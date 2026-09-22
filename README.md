````markdown name=README.md
# WeatherApp

A simple Python command-line weather application that uses the [OpenWeather API](https://openweathermap.org/api) to retrieve current weather conditions for a city.

## Features

- Accepts a city name from the command line.
- Converts the city name into geographic coordinates.
- Retrieves the current weather for the city.
- Displays:
  - City name
  - Temperature in Celsius
  - Humidity
  - Weather description
- Handles unavailable cities, connection errors, request timeouts, and API errors.

## Requirements

- Python 3.8 or later
- An OpenWeather API key
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

   On macOS or Linux:

   ```bash
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create an account at [OpenWeather](https://openweathermap.org/).
2. Generate an API key.
3. Open `Weatherapp.py`.
4. Replace both occurrences of:

   ```python
   API_key = "YOUR_API_KEY"
   ```

   with your actual API key:

   ```python
   API_key = "your_actual_api_key"
   ```

> Do not commit your API key to a public repository. For production use, store it in an environment variable instead.

## Usage

Run the application with:

```bash
python Weatherapp.py
```

Enter a city name when prompted:

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

- The city cannot be found.
- There is no internet connection.
- The request times out.
- The OpenWeather API returns an unexpected status code.

## Project Structure

```text
WeatherApp/
├── Weatherapp.py
├── requirements.txt
└── README.md
```

## License

No license has been specified for this project.
````
