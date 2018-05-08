# File with important common constants for the API scripts
# @ToDo: Consider move the KEY to a pmk or similar
KEY = "ba3288780ec658cc"
BASE_URL = "http://api.wunderground.com/api/"+ KEY +"/forecast10day/q/"
FILENAME = "simple_forecast.json"
CITIES = ["BERLIN", "HAMBURG", "MUNICH", "COLOGNE", "FRANKFURT"]

#Coordinates
coordinates = { 'BERLIN': (52.52000659999999, 13.404954),
                'MUNICH': (48.1351253,  11.5819805),
                'HAMBURG': (53.5510846, 9.9936819),
                'FRANKFURT': (50.1109221, 8.6821267),
                'COLOGNE': (50.937531, 6.9602786)
            }
