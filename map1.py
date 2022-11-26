import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

volcanoData = pandas.read_csv("./Resources/Volcanoes.txt")

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


def marker_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation > 3000:
        return "red"
    else:
        return "orange"


lat = list(volcanoData["LAT"])
lon = list(volcanoData["LON"])
elev = list(volcanoData["ELEV"])
name = list(volcanoData["NAME"])

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            radius=6,
            fill_color=marker_color(el),
            color="grey",
            fill_opacity=0.7,
            fill=True,
        )
    )

fg.add_child(
    folium.GeoJson(
        data=open("./Resources/world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            "fillColor": "green"
            if x["properties"]["POP2005"] < 10000000
            else "orange"
            if 10000000 <= x["properties"]["POP2005"] < 20000000
            else "red"
        },
    )
)

map.add_child(fg)
map.save("Map1.html")
