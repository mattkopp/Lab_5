#Matt Koppelman
#GIS501
#10/29/2014
#Lab 5 - Challenge 4


import arcpy
from arcpy import env


env.workspace = "H:/UWTacoma/GIS501/Lab_5/Data"


airports = "airports.shp"
AtRisk_lyr  = "AtRisk_lyr"
Selection = " \"SECURITY\" = 'AT RISK' "
Selection2 = " \"SECURITY\" = 'SAFE' "
airports_lyr = "airports_lyr"
AtRisk_shp = "Alaska At Risk.shp"
AtRisk_lyr2 = "AtRisk_lyr2"




arcpy.MakeFeatureLayer_management(airports, AtRisk_lyr, Selection) #Make feature layer of only At Risk Airports
arcpy.MakeFeatureLayer_management(airports, airports_lyr) #Make feature layer of all Airports


arcpy.SelectLayerByLocation_management(airports_lyr, "WITHIN_A_DISTANCE", AtRisk_lyr, "50000 meters", "NEW_SELECTION") #Select airports with 50km of At Risk Airports
arcpy.FeatureClassToFeatureClass_conversion(airports_lyr, "H:/UWTacoma/GIS501/Lab_5/Data", AtRisk_shp, "", "", "") #Convert selection to a new shapefile




arcpy.MakeFeatureLayer_management(AtRisk_shp, AtRisk_lyr2) #Create feature layer of new shapefile
arcpy.SelectLayerByAttribute_management (AtRisk_lyr2, "NEW_SELECTION", Selection2) #Select records marked as Safe from new shapefile

with arcpy.da.UpdateCursor(AtRisk_lyr2, ["SECURITY"]) as cursor:   #Use update cursor to change Security Value from SAFE to MEDIUM
	for row in cursor:
		row[0] = "MEDIUM RISK"
		cursor.updateRow(row)


arcpy.Rename_management(AtRisk_shp, "AlaskaAtRisk.shp") #Rename file to get rid of spaces
