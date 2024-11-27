
"""
Latitude : 
degré entre la position et l'équateur
    nord (+) et sud (-)

Longitude :
degré entre la position et le prime meridian
    ouest (-) et est (+)

    
écriture DMS exemple : 77° 30' 29.9988" S 	164° 45' 15.0012" E
Pour passer de l'écriture DD à DMS : 
partie entière latitude = degrés
partie entière de la partie décimale de latitude * 60 = minutes
partie décimale des minutes * 60 = secondes
direction nord (N) si postitve et sud (S) si négative

même chose pour la ongitude mais avec les directions est (E) si positive et ouest (W) si négative

"""

import numpy as np
from matplotlib import pyplot as plt

"""  Global parameters """
MIN_LATITUDE = -90.
MAX_LATITUDE = 90.
MIN_LONGITUDE = -180.
MAX_LONGITUDE = 180.

# coordinates of the area around Pougne-Hérisson (French city)
ACTIVE_MIN_LATITUDE = 46.657240
ACTIVE_MAX_LATITUDE = 46.664955
ACTIVE_MIN_LONGITUDE = -0.408307
ACTIVE_MAX_LONGITUDE = -0.387321

class Coordinate:
    """ initialisation """
    def __init__(self, latitude = 0., longitude = 0.):
        self.latitude = latitude
        self.longitude = longitude
    
    """ Returns the new coordinates after the target moved """
    def next_coordinate(self):
        delta = 0.000025 #max value to move around

        delta_latitude = np.random.uniform(-delta, delta)
        while not (in_perimeter(self.latitude + delta_latitude, self.longitude)):
            delta_latitude = np.random.uniform(-delta, delta)
        self.latitude += delta_latitude

        delta_longitude = np.random.uniform(-delta, delta)
        while not (in_perimeter(self.latitude, self.longitude + delta_longitude)):
            delta_longitude = np.random.uniform(-delta, delta)
        self.longitude += delta_longitude


    """ Return a string describing the coordinates in DD format """
    def to_string_dd(self):
        return "Latitude : " + str(self.latitude) + " , Longitude : " + str(self.longitude)
    
    """ Return a string describing the coordinates in DMS format"""
    def to_string_dms(self):
        def convert_to_dms(x):
            x = abs(x)
            degrees = int(x)
            minutes = int((x - degrees) * 60)
            seconds = round( ((x-degrees)*60 -minutes) * 60 , 2)
            return degrees, minutes, seconds

        degrees_lalitude, minutes_latitude, seconds_latitude = convert_to_dms(self.latitude)
        degrees_longitude, minutes_longitude, seconds_longitude = convert_to_dms(self.longitude)

        direction_latitude = "N" if self.latitude >= 0 else  "S"
        direction_longitude = "E" if self.longitude >= 0 else "W"

        latitude_dms = f"{degrees_lalitude}°{minutes_latitude}'{seconds_latitude}\" {direction_latitude}"
        longitude_dms = f"{degrees_longitude}°{minutes_longitude}'{seconds_longitude}\" {direction_longitude}"

        return str(latitude_dms) + " " + str(longitude_dms)
    
    """ Getters and setters """
    def set_latitude(self, latitude):
        if (MIN_LATITUDE < latitude) and (latitude < MIN_LATITUDE) and (type(latitude) == float):
            self.latitude = latitude
        else:
            print("Format ou valeur invalide, saisissez un flottant entre", MIN_LATITUDE, "et", MAX_LATITUDE)
    def get_latitude(self):
        return self.latitude
    def set_longitude(self, longitude):
        if (MIN_LONGITUDE < longitude) and (longitude < MAX_LONGITUDE) and (type(longitude) == float):
            self.longitude = longitude
        else:
            print("Format ou valeur invalide, saisissez un flottant entre", MIN_LONGITUDE, "et", MAX_LONGITUDE)
    def get_longitude(self):
        return self.longitude


""" Returns an randomly-initialized Coordinate object """
def generate_coordinate():
    latitude = np.random.uniform(ACTIVE_MIN_LATITUDE, ACTIVE_MAX_LATITUDE)
    longitude = np.random.uniform(ACTIVE_MIN_LONGITUDE, ACTIVE_MAX_LONGITUDE)
    coord = Coordinate(latitude, longitude)
    return coord

def in_perimeter(latitude, longitude):
    if (MIN_LATITUDE < latitude) and (latitude < MAX_LATITUDE) and (MIN_LONGITUDE < longitude) and (longitude < MAX_LONGITUDE):
        return True
    else:
        return False
