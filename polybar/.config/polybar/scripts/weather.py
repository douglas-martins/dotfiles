# More info about wether at - https://openweathermap.org/weather-conditions
# To show icons from this script you will need to buy "Font Awesome Pro" font - https://fontawesome.com/
# Also you can change icon in arrays to yours icons

# Configured for NerdFonts 

import requests
import json

# Settings
api_key="aa39558ba6af72ff0f0ece0d1135c570"
city="Sao+Jose,SC,BR"
lat="-27.572935893668593"
lon="-48.60687635686367"
units = "metric" # Unit system {imperial or metric}
temperature_unit = "C" # Units of measurement. That will be showed in UI. Does not affect on API.
base_url="http://api.openweathermap.org/data/2.5/weather?"

icons_list = {
    "01d": "", # Clear sky day.
    "01n": "", # Clear sky night.
    "02d": "", # Few clouds day.
    "02n": "", # Few clouds night.
    "03d": "", # Scattered clouds day.
    "03n": "", # Scattered clouds night.
    "04d": "", # Broken clouds day.
    "04n": "", # Broken clouds night.
    "09d": "", # Shower rain day.
    "09n": "", # Shower rain night.
    "10d": "", # Rain day.
    "10n": "", # Rain night
    "11d": "", # Thunderstorm day.
    "11n": "", # Thunderstorm night
    "13d": "", # Snow day. Snowflake alternative: 
    "13n": "", # Snow night. Snowflake alternative: 
    "50d": "", # Mist day.
    "50n": "" # Mist night.
}

atmophere_icons_list = {
    701: "", # Mist
    711: "", # Smoke
    721: "", # Haze
    731: "", # Dust (Sand / dust whirls)
    741: "", # Fog
    751: "", # Sand
    761: "", # Dust
    762: "", # Ash
    771: "", # Squalls
    781: ""  # Tornado
}

def main():
    try:
        query = f"lat={lat}&lon={lon}&units={units}&appid={api_key}"
        url = f"{base_url}{query}"

        result = requests.get(url)

        if (result.status_code == requests.codes['ok']):
            weather = result.json()

            w_id = int(weather['weather'][0]['id'])
            group = weather['weather'][0]['main'].capitalize()
            icon = weather['weather'][0]['icon'].capitalize()
            temp = int(float(weather['main']['temp']))

            # Load another icons for Atmosphere group
            if (group == "Atmosphere"):
                return f"{atmophere_icons_list[w_id]} {temp}°{temperature_unit}"

            return icons_list[icon] + ' %{F${foreground' + ' {}°{}'.format(temp, temperature_unit) + '%{F-}'
        else:
            return "" # Return reload icon
    except:
        return "" # Return reload icon

if __name__ == "__main__":
    print(main())