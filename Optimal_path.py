import pandas as pd
from Route_Start_End import house_work_pairs
from Create_Path_Network import river_network
import folium

river_dist_dict = {
    (row['start'], row['end']): row['distance']
    for _, row in river_network.iterrows()
}

def path_distance(path):
    if not path or len(path) <= 1:
        return 0
    return sum(
        river_dist_dict.get((path[i], path[i + 1]), 0) 
        for i in range(len(path) - 1)
    )

def get_path_distance(row):
    return path_distance(row['path'])

house_work_pairs['path_distance'] = house_work_pairs.apply(get_path_distance, axis=1)

def optimum_path(df):
    df = df.copy()
    df['score'] = df['NO UNITS_house'] * df['NO UNITS_work'] / df['path_distance']
    df.loc[df['path_distance'] < 1, 'score'] = 0
    return df['score'].idxmax()

r = optimum_path(house_work_pairs)

house_work_pairs.iloc[[r-1]].to_csv('Optimum_Path.tsv', sep='\t', index=False, header=True)

# I restricted the distance to a mile or greater just give the city a better idea of what area could use a bike path the most
# This resulted in a bike path along Dawson's Creek in a heavily populated area of Baton Rouge
# As a native of Baton Rouge I think this would be a fabulous choice for building a bike path

def plot_route(route_coords, start, end):
    route_map = folium.Map(location=[end[0], end[1]], zoom_start=11)

    # Plot Route (Polyline)
    route_polyline = [(lat, lon) for lat, lon in route_coords]
    folium.PolyLine(route_polyline, color="blue", weight=5, opacity=0.7).add_to(route_map)
    # Add Start and End Markers
    folium.Marker(
        location=start,
        popup='Start',
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(route_map)

    folium.Marker(
        location=end,
        popup='End',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(route_map)

    return route_map

# Create a map centered around the first route's start point
r = optimum_path(house_work_pairs)  # Index of the route to plot
route_coords = [(lat, lon) for lat, lon in house_work_pairs['path'][r]]
start = house_work_pairs['route_start'][r]
end = house_work_pairs['route_end'][r]
route_map = plot_route(route_coords, start, end)
