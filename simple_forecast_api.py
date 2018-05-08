import requests
import time
import json
import constants

def get_response(query):
    """
    Access wunderground API to do a get request
    """
    return requests.get(constants.BASE_URL + query+ ".json").json()


def collect_forecast_coords(coords, city):
    """
    Stores the json object corresponding to the weather forecast of city in a file.
    Parameters:
    coords: dictionary with the city names as keys, and tuple of coordinates as value
    city: name of the city in a string format 
    """
    latitude, longitude= constants.coordinates.get(city)
    location = str(latitude)+ "," + str(longitude)
    response = get_response(location)
    simple_forecast = response.get("hourly_forecast")
    filename = str(time.time()) + "_" + city + "_" + constants.FILENAME
    f = open(filename, 'w')
    json.dump(simple_forecast, f)
    f.close()

[collect_forecast_coords(constants.coordinates, city) for city in constants.coordinates.keys()]