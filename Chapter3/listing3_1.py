# Script to read attributes from a shapefile.

# Don't forget to import ogr
import sys
from osgeo import ogr

# Open the data source and get the layer
fn = r'/Users/ho/Documents/GitHub/osgeopy-code/osgeopy-data/osgeopy-data/global/ne_50m_populated_places.shp'
ds = ogr.Open(fn, 0) # second parameter = 0 for read only, =1 or True for update or edit mode
if ds is None:
    sys.exit('Could not open {0}.'.format(fn))
lyr = ds.GetLayer(0)

i = 0
for feat in lyr:

    # Get the x,y coordinates
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()

    # Get the attribute values
    name = feat.GetField('NAME')
    pop = feat.GetField('POP_MAX')
    pop = feat.GetFieldAsString('POP_MAX') # get value with changed different field types
    print(name, pop, x, y)
    i += 1
    if i == 10:
        break
# del ds


# 3.3.1
num_feature = lyr.GetFeatureCount()
last_feature = lyr.GetFeature(num_feature - 1)
print(last_feature.NAME)

feat_next = lyr.GetNextFeature().GetFID()
feat_next

lyr.ResetReading() # reset current feature
i = 0
for feat in lyr:
    fid = feat.GetFID()
    name = feat.GetField('NAME')
    print(fid, name)
    i += 1
    if i == 10:
        break

