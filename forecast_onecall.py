import argparse
import requests
import json

# Step 3: Set up the command-line interface
parser = argparse.ArgumentParser(description='Weather Forecasting Tool')
parser.add_argument('city', metavar='CITY', type=str, help='Name of the city')
args = parser.parse_args()

# Step 4: Implement the API request
API_KEY = 'e2872017f99b604bdfed100f039de44d'  # Replace 'your_api_key' with your actual API key from OpenWeatherMap
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
city = args.city

# Construct the API URL with the city name and API key as query parameters
url = f"{BASE_URL}?q={city}&appid={API_KEY}"

# Send the API request
response = requests.get(url)

# Step 5: Handle API response and errors
if response.status_code != 200:
    print(f"Error: Unable to fetch weather data for {city}. Please try again.")
    exit(1)

# Parse the JSON response
data = json.loads(response.text)

# Step 6: Extract and display weather information
weather = data['weather'][0]['description']
temperature = data['main']['temp']
humidity = data['main']['humidity']

print(f"Weather forecast for {city}:")
print(f" - Description: {weather}")
print(f" - Temperature: {temperature} K")
print(f" - Humidity: {humidity}%")
