import wget
import os
import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


def download_if_needed(URL, filename):
    """Downloads the data at the URL unless it is already stored locally"""
    if os.path.exists(filename):
        print 'File already exists'
        return
    else:
        print filename+' Downloading'
        wget.download(URL)

        
def get_pronto_data():
    """ Download pronto data unless already downloaded"""
    download_if_needed('https://s3.amazonaws.com/pronto-data/open_data_year_one.zip', 'open_data_year_one.zip')


def get_trip_data():
    """Fetch pronto data if needed and return as dataframe"""
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zf.open('2015_trip_data.csv')
    return pd.read_csv(file_handle)

def get_wx_data():
    """Fetch pronto data if needed and return weather as dataframe"""
    get_pronto_data()
    zf = zipfile.ZipFile('open_data_year_one.zip')
    file_handle = zf.open('2015_weather_data.csv')
    return pd.read_csv(file_handle)

def get_trips_and_weather():
    trips = get_trip_data()
    weather = get_wx_data()
    date = pd.DatetimeIndex(trips['starttime'])
    trips_by_date = trips.pivot_table('trip_id', aggfunc='count',
                                      columns='usertype', index=date.date)
    weather = weather.set_index('Date')
    weather = weather.iloc[:-1]
    weather.index = pd.DatetimeIndex(weather.index)
    
    return weather.join(trips_by_date)

def plot_daily_totals():
    data = get_trips_and_weather()
    fig, ax = plt.subplots(2, figsize=(14,6))

    data['Annual Member'].plot(ax=ax[0], title='Annual Member')
    data['Short-Term Pass Holder'].plot(ax=ax[1], title='Short-term Pass Holder')
