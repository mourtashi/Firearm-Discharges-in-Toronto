import pandas as pd
import geopandas as gpd
import json
from shapely.geometry import shape, MultiPoint
import folium
from folium.plugins import HeatMap, MarkerCluster

def format_popup(row):
    return f"""
    Date: {row['OCC_DATE']}<br>
    Time: {row['OCC_HOUR']}<br>
    Division: {row['DIVISION']}<br>
    Death: {"Yes" if row['DEATH'] else "No"}<br>
    Injuries: {row['INJURIES']}<br>
    Neighborhood: {row['NEIGHBOURHOOD_158']}<br>
    """


data = pd.read_csv('/Users/mustafa/Desktop/Coding Projects/Firearm Discharges In TO/RAW DATA/shootings-firearm-discharges - 4326.csv')

data['geometry'] = data['geometry'].apply(lambda x: shape(json.loads(x.replace("'", '"'))))

data['geometry'] = data['geometry'].apply(lambda x: x.geoms[0] if isinstance(x, MultiPoint) else x)

gdf = gpd.GeoDataFrame(data, geometry='geometry')

toronto_coordinates = [43.70, -79.42]
m = folium.Map(location=toronto_coordinates, zoom_start=11)

marker_cluster = MarkerCluster(name='Firearm Discharges').add_to(m)

for _, row in gdf.iterrows():
    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=format_popup(row)
    ).add_to(marker_cluster)

heatmap_data = [[row.geometry.y, row.geometry.x] for _, row in gdf.iterrows()]

HeatMap(heatmap_data, name='Heatmap').add_to(m)

folium.LayerControl().add_to(m)

m.save('/Users/mustafa/Desktop/Coding Projects/Firearm Discharges In TO/Processed Data/toronto_firearm_discharges_heatmap.html')
