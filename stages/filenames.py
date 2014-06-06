"""
Script to extract location information from photograph metadata
and export it into a CSV file.
"""

import glob
import os
import sys

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

