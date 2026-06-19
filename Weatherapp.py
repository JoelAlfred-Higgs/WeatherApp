import requests
def coord(name):
    headers = {                
        "content-type":"application/json"
    } 
    API_key = "YOUR_API_KEY"
    try:
        res = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid={API_key}",headers=headers)
        if res.status_code == 200:
           data = res.json()
           if not data:
                print("City not found!")
                return None, None
           return data[0]["lat"],data[0]["lon"]
           
        elif res.status_code == 404:
            print("City not found!")
        else:
            print(f"Error:{res.status_code}")
    
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.Timeout:
        print("request timed out")

def weather(lat,lon):
    API_key = "YOUR_API_KEY"
    headers = {
        "content-type":"application/json"
    } 
    try:
        res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric",headers=headers)
        if res.status_code == 200:
           data = res.json()
           print(f"City: {data['name']}")
           print(f"Temperature: {data['main']['temp']} °C")
           print(f"Humidity: {data['main']['humidity']} %")
           print(f"Weather: {data['weather'][0]['description']}")
        elif res.status_code == 404:
            print("City not found!")
        else:
            print(f"Error:{res.status_code}")
    except requests.exceptions.ConnectionError:
        print("No internet connection")
    except requests.exceptions.Timeout:
        print("request timed out")
         
    
city_name = input("Enter city name: ")
lat,lon = coord(city_name)
if lat is not None and lon is not None:
    weather(lat,lon)


