# waterLining
python script for ArcGIS to create water lines or shoreline vignette
This script is for ArcGIS using the ArcPy module. The method produces results similar to the water bodies in older USGS topo maps. 
It creates buffers from the shoreline at an expondential distance, using parameters set by user. 
<br><br>
Historical Topo with water lining<br>
<img height="400" width="auto" src="http://www.esri.com/news/arcnews/fall09articles/fall09gifs/p12p1-lg.jpg" alt="old USGS topo with water lining")/> 
<br><br>
Output using this script for Arc.<br>
<img height="400" width="auto" src="http://i.imgur.com/1cbsN9H.png")/>

The script creates data... it is not just a layer 'effect'. This could be problematic if you are working on a huge amount of shoreline or do not want to store more data. 