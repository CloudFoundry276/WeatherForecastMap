from folium import Map, Marker, Popup
from geo import Geopoint


# Get latitude & longitude values
locations = [
    [-31.9523, 115.8613],
    [-12.4637, 130.8444],
    [-34.9285, 138.6007],
    [-37.8136, 144.9631],
    [-16.9203, 145.7710],
    [-42.8826, 147.3257],
    [-35.2809, 149.1300],
    [-33.8688, 151.2093],
    [-27.4705, 153.0260],
    [-28.0167, 153.4000]
]

# Map Instance
mymap = Map(location=[-27.67315, 134.63065])

# starts for loop
for lat, lon in locations:
    """Create a Geopoint Instance"""
    geopoint = Geopoint(latitude=lat, longitude=lon)
    forecast = geopoint.get_weather()
    popup_content = f"""
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°C <img src='http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png' width=35 />
    <hr style='margin: 1px;'>
    {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}°C <img src='http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png' width=35 />
    <hr style='margin: 1px;'>
    {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}°C <img src='http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png' width=35 />
    <hr style='margin: 1px;'>
    {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}°C <img src='http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png' width=35 />
    """

    # Create Popup object & add it to geopoint
    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)

# Save the map instance into html file
mymap.save("map.html")
