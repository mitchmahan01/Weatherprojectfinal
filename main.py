import json
import requests

# Uses API key to search by city for the user to find weather
base_url_by_city = "http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=imperial"

# Weather API Key
api_key = '70d9c51e7360a54d4e27fc8462f05784'

def get_state(city_name):
    geolocation_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    response = requests.get(geolocation_url)
    data = response.json()
    if response.status_code == 200 and data:
        state = data[0].get("state")
        return state
    return None

while True:
    print("How would you like to search for weather information?")
    print("1. Search by zip code")
    print("2. Search by city")
    print("3. Quit")

    user_choice = input("Enter your choice (1, 2, 3, or Q to quit): ").strip().lower()

    if user_choice == '1':
        zip_code = input("Please enter the zip code: ")
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&appid={api_key}&units=imperial"
    elif user_choice == '2':
        city_name = input("Please enter the city name: ")
        url = base_url_by_city.format(CITY_NAME=city_name, API_KEY=api_key)
    elif user_choice == '3' or user_choice == 'q':
        print("Quitting...")
        exit()
    else:
        print("Invalid choice. Please try again.")
        continue

    print()

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Display city, state, country information
        city = data["name"]
        state = get_state(city)
        print(f"Location: {city}, {state}")

        # Max and min temperature of specified location
        temp_max = data["main"]["temp_max"]
        temp_min = data["main"]["temp_min"]
        print(f"Max Temperature: {temp_max}°F")
        print(f"Min Temperature: {temp_min}°F")

        # Wind details of specified location
        wind_speed = data["wind"]["speed"]
        wind_deg = data["wind"]["deg"]
        print(f"Wind Speed: {wind_speed} mph")
        print(f"Wind Direction: {wind_deg}°")
    else:
        print("Error retrieving weather data. Please try again.")

    print()
