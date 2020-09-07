# This is a project where people can view the volcanoes in the US, and they can view the populations


import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

names = list(data["NAME"])
locations = list(data["LOCATION"])
status = list(data["STATUS"])
elevations = list(data["ELEV"])
types = list(data["TYPE"])


def color_producer(elevation):
    if elevation < 1000:
        return "yellow"
    elif 1000 <= elevation < 3000:
        return "blue"
    else:
        return "red"


map3 = folium.Map(location=[36.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

featureGroupV = folium.FeatureGroup(name="Volcanoes")

for lt, ln, elev in zip(lat, lon, elevations):
    featureGroupV.add_child(
        folium.CircleMarker(location=(lt, ln), popup=str(elev) + "m", radius=6, fill_color=color_producer(elev),
                            color=color_producer(elev), fill_opacity=0.7))
featureGroupP = folium.FeatureGroup(name="Population")

featureGroupP.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                       style_function=lambda x: {
                                           'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                           else 'orange' if 10000000 <= x["properties"][
                                               "POP2005"] < 20000000 else 'red'}))

map3.add_child(featureGroupV)
map3.add_child(featureGroupP)

map3.add_child(folium.LayerControl())

map3.save("Map1HE.html")
