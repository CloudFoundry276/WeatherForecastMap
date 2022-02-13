from folium import Marker
from hawamaan import Weather


class Geopoint(Marker):
    def __init__(self, latitude, longitude, popup=None):
        super().__init__(location=[latitude, longitude], popup=popup)
        self.latitude = latitude
        self.longitude = longitude

    def get_weather(self):
        weather = Weather(apikey="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", lat=self.latitude, lon=self.longitude)
        return weather.next_12h_simplified()
