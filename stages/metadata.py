"""
Script to extract location information from photograph metadata
and export it into a CSV file.
"""

import glob
import os
import sys

import pyexiv2

# Constants for the EXIF keys we will extract.
LATITUDE = "Exif.GPSInfo.GPSLatitude"
LATITUDE_REF = "Exif.GPSInfo.GPSLatitudeRef"
LONGITUDE = "Exif.GPSInfo.GPSLongitude"
LONGITUDE_REF = "Exif.GPSInfo.GPSLongitudeRef"
MAKE = "Exif.Image.Make"
MODEL = "Exif.Image.Model"
TIMESTAMP = "Exif.Image.DateTime"

# Extract command-line arguments.
source = sys.argv[1]
target = sys.argv[2]

# Verify that the source path exists.
if not os.path.isdir(source):
    print "Source does not exist."
    sys.exit(1)

# Display the source and target.
print "Source:", source
print "Target:", target

# List all JPEG files in the source.
pattern = os.path.join(source, "*.jpg")
filenames = glob.glob(pattern)

# Display the list of filenames.
print "Filenames:", filenames

# Extract the photograph metadata into a table.
table = []
for photograph in filenames:
    
    # Read the metadata from the photograph.
    metadata = pyexiv2.ImageMetadata(photograph)
    metadata.read()

    # Extract the location in degrees, minutes, and seconds.
    lat_deg, lat_min, lat_sec = metadata[LATITUDE].value
    lon_deg, lon_min, lon_sec = metadata[LONGITUDE].value
    
    # Convert the degrees, minutes, and seconds to decimal.
    latitude = (lat_deg + (lat_min / 60.0) + (lat_sec / 3600.0))
    longitude = (lon_deg + (lon_min / 60.0) + (lon_sec / 3600.0))
    if metadata[LATITUDE_REF].value != "N":
        latitude *= -1
    if metadata[LONGITUDE_REF].value != "E":
        longitude *= -1

    # Extract descriptive information from the metadata.
    make = metadata[MAKE].value
    model = metadata[MODEL].value
    timestamp = metadata[TIMESTAMP].value

    # Extract the name of the photograph from its full path.
    name = os.path.basename(photograph)

    # Add the information to the table.
    table.append((name, timestamp, make, model, latitude, longitude))

# Display the table of photograph metadata.
print "Table:", table

