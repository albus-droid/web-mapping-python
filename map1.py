import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

volcanoData = pandas.read_csv("./Resources/Volcanoes.txt")

lat = list(volcanoData["LAT"])
lon = list(volcanoData["LON"])
elev = list(volcanoData["ELEV"])

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(str(el) + "m", parse_html=True),
            icon=folium.Icon(color="green"),
        )
    )

map.add_child(fg)
map.save("Map1.html")
