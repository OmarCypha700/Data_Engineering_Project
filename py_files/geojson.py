
# Import libraries
import pandas as pd
import json

# Read csv file
df = pd.read_csv('data/locations.csv')

# Convert data to dictionary
location_data = df.to_dict(orient='records')
location_data

# Convert to GeoJSON
geojson = {
    "type": "FeatureCollection",
    "features": []
}

for data in location_data:
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [data["lon"], data["lat"]]
        },
        "properties": {
            "epoch": data["epoch"],
            "elevation": data["elevation"]
        }
    }
    geojson["features"].append(feature)

with open("data/geo.json", "w") as f:
    json.dump(geojson, f, indent=2)
