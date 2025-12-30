import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
def get_latitude_longitude(location):
    geo_api = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1"
    geo_response = requests.get(geo_api)
    
    if geo_response.status_code!=200:
        print("Failed to fetch location data")
        exit()
    
    geo_data = geo_response.json()
    
    if "results" not in geo_data:
        print("City not found")
        exit()

    return geo_data["results"][0]["latitude"], geo_data["results"][0]["longitude"]

def get_temperature(latitude, longitude):
    temp_api = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    temp_response = requests.get(temp_api)

    if temp_response.status_code != 200:
        print("Failed to fetch weather data")
        exit()

    temp_data = temp_response.json()

    return temp_data["current"]["temperature_2m"]

def get_past_n_days_max_min_temperature(latitude, longitude, days):
    today = datetime.now()
    week_ago = today - timedelta(days)

    # Format dates for API (YYYY-MM-DD)
    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    temp_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

    response = requests.get(temp_url)
    data = response.json()
    return data["daily"]

def json_to_dataframe(data):
    df = pd.DataFrame({
        'data': data['time'],
        'max_temperature': data['temperature_2m_max'],
        'min_temperature': data['temperature_2m_min']
    })

    # Convert date strings to datetime
    df['date'] = pd.to_datetime(df['date'])
    return df

def 
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Paris Weather - Past 7 Days')
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()


location = "Vijayawada"
latitude, longitude = get_latitude_longitude(location)
curr_temperature = get_temperature(latitude,longitude)
data = get_past_n_days_max_min_temperature(latitude,longitude, 7)
df = json_to_tablular(data)

#--------------------------------
#Get Past n - days temperatures


