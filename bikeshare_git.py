import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US Bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to filter by? (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose from Chicago, New York City, or Washington.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? (all, January, February, March, April, May, June): ").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid input. Please choose a month between January and June, or 'all' for no filter.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "Which day of the week? (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid input. Please choose a day of the week or 'all' for no filter.")

    print('=' * 60)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime and create 'month' and 'day_of_week' columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Apply filters directly while extracting relevant columns
    if month != 'all':
        month_numbers = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
        df = df[df['Start Time'].dt.month == month_numbers[month]]

    if day != 'all':
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas DataFrame containing the data
        month - name of the month selected by user or "all"
        day - name of the day of week selected by user or "all"
    """

    print('\n' + '='*20 + ' Time Stats ' + '='*20)
    start_time = time.time()

    if not df.empty:
        # Most common month
        if month == "all" and 'Start Time' in df:
            common_month = df['Start Time'].dt.month.mode()[0]
            print(f"\nMost Common Month: {common_month}")
        else:
            print(f"\nFilter by Month: {month.capitalize()}")

        # Most common day of the week
        if day == "all":
            common_day_of_week = df['Start Time'].dt.day_name().mode()[0]
            print(f"Most Common Day of Week: {common_day_of_week}")
        else:
            print(f"Filter by Day of Week: {day.capitalize()}")

        # Most common hour
        common_hour = df['Start Time'].dt.hour.mode()[0]
        print(f"Most Common Start Hour: {common_hour}")
    else:
        print("\nNo data available for analysis.")

    print(f"\nProcess completed in {time.time() - start_time:.2f} seconds.")
    print('=' * 60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n' + '='*20 + ' Station Stats ' + '='*20)
    start_time = time.time()

    if not df.empty:
        # Most common start station
        common_start_station = df['Start Station'].mode()[0] if 'Start Station' in df else "N/A"
        print(f"\nMost Commonly Used Start Station: {common_start_station}")

        # Most common end station
        common_end_station = df['End Station'].mode()[0] if 'End Station' in df else "N/A"
        print(f"Most Commonly Used End Station: {common_end_station}")

        # Most frequent combination of start and end station
        if 'Start Station' in df and 'End Station' in df:
            common_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
            print(f"Most Frequent Combination of Start and End Station Trip: {common_trip}")
        else:
            print("\nNo data available for station combinations.")
    else:
        print("\nNo data available for analysis.")

    print(f"\nProcess completed in {time.time() - start_time:.2f} seconds.")
    print('=' * 60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n' + '='*20 + ' Trip Duration Stats ' + '='*20)
    start_time = time.time()

    if not df.empty and 'Trip Duration' in df:
        total_travel_time = df['Trip Duration'].sum()
        mean_travel_time = df['Trip Duration'].mean()
        print(f"\nTotal Travel Time: {total_travel_time:,} seconds")
        print(f"Average Travel Time: {mean_travel_time:.2f} seconds")
    else:
        print("\nNo trip duration data available.")

    print(f"\nProcess completed in {time.time() - start_time:.2f} seconds.")
    print('=' * 60)


def user_stats(df):
    """Displays statistics on Bikeshare users."""

    print('\n' + '=' * 25 + ' User Stats ' + '=' * 25)
    start_time = time.time()

    # Display counts of user types
    print('\nUser Types:')
    user_types = df['User Type'].value_counts()
    for user_type, count in user_types.items():
        print(f"  {user_type}: {count:,}")

    # Display counts of gender (only if available in the dataset)
    if 'Gender' in df.columns:
        print('\nGender Counts:')
        gender_counts = df['Gender'].value_counts()
        for gender, count in gender_counts.items():
            print(f"  {gender}: {count:,}")
    else:
        print("\nNo gender data available for this city.")

    # Display earliest, most recent, and most common year of birth (only if available in the dataset)
    if 'Birth Year' in df.columns:
        print('\nYear of Birth Statistics:')
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"  Earliest Year of Birth: {earliest_year}")
        print(f"  Most Recent Year of Birth: {most_recent_year}")
        print(f"  Most Common Year of Birth: {most_common_year}")
    else:
        print("\nNo birth year data available for this city.")

    print(f"\nProcess completed in {time.time() - start_time:.2f} seconds.")
    print('=' * 60)


def display_raw_data(df):
    """Displays raw data 5 rows at a time upon user request."""

    # Set options to display all columns
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', None)        # Don't limit the width

    start_loc = 0
    # Get the total number of rows in the dataframe
    total_rows = df.shape[0]

    while start_loc < total_rows:
        # Prompt the user if they want to see raw data
        user_input = input(f"\nDo you want to see the next 5 rows of data? (yes or no): ").strip().lower()
        if user_input == 'yes':
            # Display next 5 rows of data
            end_loc = min(start_loc + 5, total_rows)
            print(df.iloc[start_loc:end_loc])
            start_loc += 5

            # Check if we reached the end of the dataframe
            if start_loc >= total_rows:
                print("\nYou've reached the end of the data.")
                break
        elif user_input == 'no':
            print("\nExiting raw data display...")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Reset options to defaults
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
