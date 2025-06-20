# Optimum_Bike_Path
This project optimizes the most efficient bike path in Baton Rouge, Louisiana from residential to business areas along publicly owned drainage areas represented by river and streams. East Baton Rouge Parish tax roll and parcel data were used to determine the type of structure (commercial or residential), the number of units within each structure, and location of properties that would be the start and end locations of each route. Properties were aggregated using DBSCAN with epsilon set to 250 meters for residential and 150 meters for commercial. Commercial properties were more sporatic so a smaller epsilon was more appropriate. The closest point on the river and stream paths (euclidean distance) to each residential and commercial area were defined as the start and end points, respectively. The optimal bike route was chosen by reducing distance above 1 mile and maximizing number of units within residential and commercial properties. The html code in this repository will show both the river paths and the optimal bike path (red) when the repository is cloned and a local server is open.  
Data sources:  
River and stream line paths - https://hub.arcgis.com/datasets/esri::usa-rivers-and-streams/explore  
East Baton Rouge Parish Tax Parcels - https://catalog.data.gov/dataset/tax-parcel-52918  
East Baton Rouge Parish Tax Roll - https://catalog.data.gov/dataset/ebrp-tax-roll  

To run code in order use:
1. Create_Property_Clusters
2. Create_Path_Network
3. Route_Start_End
4. Optimal_path
5. Bike_Route_Map.html

Without sharing an API key I could not load the USA_Rivers_and_Streams.geojson into the code remotely and I could not store it in github because it is too large. It is better to add it to the repository file after cloning. 
