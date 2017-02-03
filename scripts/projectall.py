import os

for filename in os.listdir("."):
    if ".shp" in filename:
        cmd = 'ogr2ogr -f "ESRI Shapefile"  unprojected/' + filename + ' ' + filename + ' -t_srs EPSG:4326'
        os.system(cmd)
