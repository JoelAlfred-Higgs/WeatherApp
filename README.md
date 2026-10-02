# WeatherApp

A simple Python command-line weather application that uses the OpenWeather API to look up a city and display the current weather conditions.

## Features

- Accepts a city name from the command line.
- Converts the city name to latitude and longitude using the OpenWeather geocoding API.
- Fetches the current weather for that location.
- Displays:
  - city name
  - temperature in Celsius
  - humidity percentage
  - weather description
- Gracefully handles invalid cities, missing internet access, timeouts, and unexpected API responses.

## Requirements

- Python 3.8 or later
- OpenWeather API keys for both geocoding and weather requests
- Internet connection

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/JoelAlfred-Higgs/WeatherApp.git
   cd WeatherApp
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create an account at [OpenWeather](https://openweathermap.org/).
2. Generate an API key.
3. Set the required environment variables before running the app.

   macOS/Linux:

   ```bash
   export API_KEY_COORD="your_geocoding_api_key"
   export API_KEY_weather="your_weather_api_key"
   ```

   Windows PowerShell:

   ```powershell
   $env:API_KEY_COORD = "your_geocoding_api_key"
   $env:API_KEY_weather = "your_weather_api_key"
   ```

   If you use the same key for both services, you can assign the same value to both variables.

> Do not commit API keys to a public repository. For a production app, consider storing them in a secure environment or secret manager.

## Usage

Run the application with:

```bash
python Weatherapp.py
```

When prompted, enter a city name:

```text
Enter city name: London
City: London
Temperature: 15.4 °C
Humidity: 76 %
Weather: overcast clouds
```

## Dependencies

The project uses:

- `requests==2.32.5`

## Error Handling

The application reports errors when:

- the city cannot be found
- there is no internet connection
- the request times out
- the OpenWeather API returns an unexpected status code

## Project Structure

```text
WeatherApp/
├── Weatherapp.py
├── requirements.txt
├── README.md
└── .gitignore
```

## License

No license has been specified for this project.
