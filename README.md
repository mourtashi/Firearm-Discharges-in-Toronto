# Firearm-Discharges-in-Toronto: Visualization Tool

This Python program provides an interactive visualization tool for exploring firearm discharges incidents in the city of Toronto, Canada. The data is displayed on an interactive map and includes a heatmap layer to highlight areas with a higher concentration of discharges. Each discharge incident is marked with a location marker that includes detailed information about the incident.

Overview:

This tool is designed to provide visual insights into firearm discharge incidents in Toronto. The main components of the program are:
1.	Data loading and processing: The tool loads and processes data from a CSV file, which contains information about each firearm discharge incident, including the geographic coordinates and other details such as date, time, division, whether it resulted in death, number of injuries, and neighbourhood.
2.	Interactive Map: The program creates an interactive map using the Folium library in Python. The map is centered around Toronto and allows users to zoom in and out and navigate to different parts of the city. 
3.	Incident Markers: Each firearm discharge incident is represented by a marker on the map. Clicking on a marker opens a popup displaying detailed information about the incident.
4.	Heatmap Layer: The tool includes a heatmap layer on the map, representing the concentration of firearm discharges across the city. This feature provides a quick visual way to identify areas with higher incidents of firearm discharges.
5.	Layer Control: The program includes a layer control feature, allowing users to toggle visibility of the marker cluster and heatmap layers.
6.	Saving the Map: The final map is saved as an HTML file, which can be opened in any web browser for viewing or shared with others.

Usage:

This tool is intended for use by anyone interested in understanding the spatial distribution and concentration of firearm discharge incidents in Toronto. This could include law enforcement, city planners, researchers, or concerned citizens.
Please note that the tool requires the following Python libraries: pandas, geopandas, json, shapely, folium, and folium.plugins.

Data Source:

The data used by this tool comes from the Toronto Public Open Data set, the complete data set can be found here: https://open.toronto.ca/dataset/shootings-firearm-discharges/

Result:

After running the script, you'll find an HTML file named toronto_firearm_discharges_heatmap.html in the specified location. You can open this file in any modern web browser to view the interactive map and explore the firearm discharge incidents.
