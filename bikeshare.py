import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_user_selection(prompt, keys):
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in keys:
            return user_input
        else:
            print(f"invalid input, pls try in {keys}")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_user_selection("name of city: ", CITY_DATA.keys())

    # get user input for month (all, january, february, ... , june)
    month = get_user_selection("name of month to filter, all to apply no filter: ", MONTHS)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_user_selection("name of day to filter, all to apply no filter: ", DAYS)


    print('-'*40)
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
    start_time = time.time()

    df = pd.read_csv(CITY_DATA[city])
    df['time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['time'].dt.month
    df['weekday'] = df['time'].dt.day_name()
    df['start_hour'] = df['time'].dt.hour

    if (month != 'all'):
        df = df[df['month'] == MONTHS.index(month)]
    
    if (day != 'all'):
        df = df[df['weekday'] == day.title()]

    
    print(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]

    # display the most common day of week
    most_common_day_of_week = df['weekday'].mode()[0]

    # display the most common start hour
    most_common_start_hour = df['start_hour'].mode()[0];

    print(f"Most common month = {most_common_month}")
    print(f"Most common day of week = {most_common_day_of_week}")
    print(f"Most common start hour = {most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    most_frequent_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()

    print(f"Most common start station = {most_common_start_station}")
    print(f"Most common end station = {most_common_end_station}")
    print(f"Most frequent trip = {most_frequent_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_time = df['Trip Duration'].mean()

    print(f"Total travel duration = {total_time}")
    print(f"Avg travel duration = {mean_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()

    # Display counts of gender
    gender_count = df['Gender'].value_counts() if 'Gender' in df.columns else None

    # Display earliest, most recent, and most common year of birth

    print(f"Count for User Type\n{user_type_count}")
    if not (gender_count is None):
        print(f"Count for Gender\n{gender_count}")
    else:
        print("Gender not available")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
