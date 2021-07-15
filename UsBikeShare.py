



import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:/Users/moemenmo/Desktop/desktop/chicago.csv',
              'new york city': 'C:/Users/moemenmo/Desktop/desktop/new_york_city.csv',
              'washington': 'C:/Users/moemenmo/Desktop/desktop/washington.csv' }

def get_filters():
    
    
    """
        Asks user to specify a city, month, and day to analyze.

         Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # specify valid lists for three inputs 
    
    
    #valid_city=['chicago','new york city','washington']
    #valid_month=['january','february','march','april','may','june','july','august','september','october','november','december','all']
    valid_day=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','All']
    valid_city=['Chicago','New York City','Washington']
    valid_month=['January','February','March','April','May','June','July','August','September','October','November','December','All']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid
    city = input("Please choose a city to study: ").title()
    print(city)
    while city not in valid_city:
        city=input("please enter a valid city: ").title()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please specify a month: ").title()
    while month not in valid_month:
        month=input("please enter a valid full month name :").title()

        
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please specify a day: ").title()
    while day not in valid_day:
        day=input("please enter a valid full weekday name :").title()
    
    city=city.lower()
    month=month.lower()
    day=day.title()
    

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
    df=pd.read_csv(CITY_DATA[city])
    valid_month=['january','february','march','april','may','june','july','august','september','october','november','december','all']
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    
    #filter dataframe by month and day
    
    #ind=valid_month.index(month)+1
    #df=df.loc[df['month']==ind]
    #df=df.loc[df['day']==day]
    
    
    if month != 'all' :
        ind=valid_month.index(month)+1
        df=df.loc[df['month']==ind]
        
    if day != 'All':
        df=df.loc[df['day']==day]
        
        
    
    
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    valid_month=['january','february','march','april','may','june','july','august','september','october','november','december']
    #print(df['month'].mode()[0])
    ind=int(df['month'].mode()[0])-1 
    popular_month=valid_month[ind]
    print('Most common month: ',popular_month)
    

    # TO DO: display the most common day of week
    print('Most common day of week: ',df['day'].mode()[0])

    # TO DO: display the most common start hour
    print('Most common start hour: ',df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station: ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('Most common end station: ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['common']=df['Start Station']+","+df['End Station']
       
    print('Most common combination of stations: ', df['common'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time']=pd.to_datetime(df['End Time'])
    df['travel duration']=df['End Time']-df['Start Time']
    
    print('Total travel time: ',df['travel duration'].sum())


    # TO DO: display mean travel time
    print('Average travel time: ',df['travel duration'].mean())

    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Count of user types :\n',df['User Type'].value_counts())


    # TO DO: Display counts of gender
    print('Count of user types :\n',df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    Earliest=int(df['Birth Year'].min())
    if Earliest < 1950:
        print('Earliest year of birth',Earliest, "seems like an entry error!!")
    else:
        print('Earliest year of birth :',Earliest)
        
    
    print('Most recent year of birth :',int(df['Birth Year'].max()))
    print('Most common year of birth :',int(df['Birth Year'].mode()[0]))
    

    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats_wash(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    print('Count of user types :\n',df['User Type'].value_counts())
    
    print('Sorry, No Gender info or Birth dates provided for washington !')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data != 'no'):
        print(df.iloc[range(0,start_loc+5)])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    
def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        
        if df.size == 0 :
            print(df)
            print('No such valid combination of month and day in the data set!')
            print('*'*40)
            continue
        else:
            if city == 'washington':
                print(df)
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats_wash(df)
                
                
            else:
                print(df)
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
                
                
            
            
    
        
            
        

        
        
        
            
        
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


