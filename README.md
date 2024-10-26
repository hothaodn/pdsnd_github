# Explore US Bikeshare Data
Updated

## Project Overview
This project explores data from bike share systems in three major cities in the United States: Chicago, New York City, and Washington, D.C. Using Python, we analyze the data to uncover insights about bike share usage patterns.

The project aims to answer several questions about the bikeshare data, such as the most popular travel times, popular stations, trip duration, and user demographics.

## Files
- **bikeshare.py**: Contains all the functions and logic for analyzing the bikeshare data.
- **README.md**: This file, providing an overview of the project and its contents.
- **Data files**: The CSV files containing the bike share data for each city:
    - chicago.csv
    - new_york_city.csv
    - washington.csv

## Project Details
The project consists of the following key components:

1. **Data Loading and Filtering**: The program allows users to specify a city, month, and day of the week to filter the data accordingly.
2. **Data Analysis**: The script computes and displays various descriptive statistics:
    - Popular travel times (most common month, day of the week, and hour).
    - Popular stations and trips (most common start/end stations and trip combinations).
    - Trip duration statistics (total and average trip duration).
    - User information (counts by user type, gender, and birth year).
3. **Interactive Raw Data Display**: Users can request to view raw data in increments of 5 rows at a time.

## Requirements
To run this project, you need the following software and packages installed:

- Python 3.x
- Pandas
- NumPy

### Optional Tools:
- A text editor like Sublime Text or Atom.
- A terminal application like Git Bash (for Windows) or Terminal (for macOS/Linux).

## How to Run the Project
1. **Download the Project Files**: Ensure that all necessary files (Python script and CSV data files) are in the same directory.
2. **Install Required Libraries**: Install Python and the required packages (Pandas and NumPy). You can do this using the following commands:
   ```bash
   pip install pandas numpy