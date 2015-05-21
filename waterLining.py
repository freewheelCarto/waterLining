#~~~~Python script for quickly creating a water body vignette in Arc.
#~~~~Set up for use in an Arc toolbox. 

import arcpy
import math
import os

#Get variables
workspace = arcpy.GetParameterAsText(0)
waterbody = arcpy.GetParameterAsText(1)
waterName = arcpy.GetParameterAsText(2)
base = arcpy.GetParameter(3) #long int
steps = arcpy.GetParameter(4) #long int
power = arcpy.GetParameter(5) #double

#set workspace
arcpy.env.workspace = workspace

arcpy.AddMessage("Creating buffers based on base and steps...")

#Complete buffer analysis using user-defined parameters
def waterLining (base, steps):
    count=1
    for x in range(0,steps):
        #formula to calculate intervals between lines. is negative for Arc buffering inside polygon
        distance = -(base*math.exp(power*count))+base
        #same formula as above but positive for adding to attribute table.
        distancePos = (base*math.exp(power*count))+base
        arcpy.Buffer_analysis(waterbody, "buffer"+waterName+str(count), distance,"OUTSIDE_ONLY","ROUND","ALL")
        arcpy.AddField_management("buffer"+waterName+str(count), "bufferDist", "FLOAT")
        arcpy.CalculateField_management("buffer"+waterName+str(count), "bufferDist", distancePos, "PYTHON_9.3")
        count=count+1
        
waterLining(base, steps)

arcpy.AddMessage("Merging buffers...")

#Merge buffer feature classes to single feature class and delete individuals
fClasses = []
i=0

fcs = arcpy.ListFeatureClasses("buffer*")

for fc in fcs:
    fClasses.append(fc)
    i=i+1

arcpy.Merge_management(fClasses, "waterLines"+waterName)

arcpy.AddMessage("Deleting individual buffer feature classes...")

for feature in fClasses:
    arcpy.Delete_management(feature)

arcpy.AddMessage("Finished creating water lines!")    
