import time
import pandas as pd

# another additonal idea to make entering data easier for the user : give every city and month and day a number , for example : chicago : 1 , june : 6 , sunday : 2
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city you want to see their data ? (Chicago, New York, , Washington )').lower()
    while city not in(CITY_DATA.keys()):
        print('Wrong city name \n Try Again ...')
        city = input('Which city you want to see their data ? (Chicago, New York, , Washington )').lower()

    # get user input if he want to filter data ( OPTINOL )
    filter = input('Would you like to filter the data by month, day, both, or none? ').lower()
    while filter not in(['month', 'day', 'both', 'none']):
        print('Wrong ENTERING name \n Try Again ...')
        filter = input('Would you like to filter the data by month, day, both, or none? ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    if filter == 'month' or filter == 'both':
        month = input('Which month you want ? ( January to june ) ').lower()
        while month not in months:
            print('Wrong city name \n Try Again ...')
            month = input('Which month you want ? ( January to june ) ').lower()
    else:
        month = 'all'


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    if filter == 'day' or filter == 'both':
        day = input('Which day you want ? ( sunday to saturday ) ').lower()
        while day not in days:
            print('Wrong day name \n Try Again ...')
            day = input('Which day you want ? ( sunday to saturday ) ').lower()
    else:
        day = 'all'

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
    # load data files
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()



    if month != 'all':
        # listing month by index
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month
        df = df[df['month'] == month]


    if day != 'all':
        # filter by day of week
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}')

    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print(f'The most common day of week is: {day}')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'The most common start hour is: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'The most popular start station is: {common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'The most popular end station is: {common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df['Start Station'] + ' to ' + df['End Station']
    print(f'The most popular trip is: from {common_trip.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    from datetime import timedelta as td
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel time :', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Avrg Travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest of Birth Year:', df['Birth Year'].min())
        print('Most Recent of Birth Year:', df['Birth Year'].max())
        print('Most Common of Birth Year:', df['Birth Year'].mode()[0])

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

        # To impelemnt for user want to see the raw data :
        enter = ['yes', 'no']
        user_input = input('do you like to see more data ? ( Yes or No)')

        while user_input.lower() not in enter:
            user_input = input('Please Enter Yes or No ')
            user_input = user_input.lower()
        a = 0
        while True:
            if user_input.lower() == 'yes':

                print(df.iloc[a : a + 5])
                a += 5
                user_input = input('do you like to see more data ? (Yes or No)')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No')
                    user_input = user_input.lower()
            else:
                break


if __name__ == "__main__":
	main()