#Matt Koppelman
#GIS501
#10/29/2014
#Lab 5 - Challenge 3



import arcpy
from arcpy import env
env.workspace = "H:/UWTacoma/GIS501/Lab_5/Data"



airports = "airports.shp"
roads = "roads.shp"
airports_lyr = "airports_lyr"


arcpy.MakeFeatureLayer_management(airports, airports_lyr)
arcpy.SelectLayerByLocation_management (airports_lyr, "WITHIN_A_DISTANCE", roads, "10000 meters", "NEW_SELECTION")
arcpy.AddField_management(airports_lyr, "SECURITY", "TEXT", "", "", 20)


with arcpy.da.UpdateCursor(airports_lyr, ["SECURITY"]) as cursor:
	for row in cursor:
		row[0] = "AT RISK"
		cursor.updateRow(row)
		




arcpy.SelectLayerByLocation_management ("airports_lyr", "WITHIN_A_DISTANCE", roads, "10000 meters", "SWITCH_SELECTION")

with arcpy.da.UpdateCursor(airports_lyr, ["SECURITY"]) as cursor:
	for row in cursor:
		row[0] = "SAFE"
		cursor.updateRow(row)



