import folium

map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

coordinate_X_Y = [[25.3170, 51.5124], [-25.578599066224918, 27.16070830821991],
                  [-26.234807275577644, 27.982478141784668], [38.2, -99.1]]
for coordinates in coordinate_X_Y:
    fg.add_child(
        folium.Marker(
            location=coordinates,
            popup="Hi I'm a Marker",
            icon=folium.Icon(color="green"),
        )
    )
map.add_child(fg)
map.save("Map1.html")
