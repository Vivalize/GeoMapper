import sys
#normSysPaths = ['/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/usr/local/lib/python3.7/site-packages', '/usr/local/Cellar/numpy/1.14.5_1/libexec/nose/lib/python3.7/site-packages']
#for i in normSysPaths: sys.path.append(i)
sys.path = ['/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/usr/local/lib/python3.7/site-packages', '/usr/local/Cellar/numpy/1.14.5_1/libexec/nose/lib/python3.7/site-packages']

import overpy
import numpy as np
import requests
from osgeo import gdal
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = 1000000000
api = overpy.Overpass()

terrainPath = None
for i in sys.argv:
	if i[-4:] == '.adf': terrainPath = i
if terrainPath != None: terrainArray = gdal.Open(terrainPath).ReadAsArray()

def getElevation(lat, lon):
	if terrainPath == None:
		urlRequest = 'https://nationalmap.gov/epqs/pqs.php?x='+str(float(lon))+'&y='+str(float(lat))+'&units=feet&output=json'
		req = requests.get(url = urlRequest)
		return req.json()['USGS_Elevation_Point_Query_Service']['Elevation_Query']['Elevation']
	else:
		zone = terrainPath.split('/')[-2][3:-3]
		eastSplit = zone.split('e')
		westSplit = zone.split('w')
		if len(eastSplit) > 1:
			lonLeft = int(eastSplit[-1])
			ns = eastSplit[0]
		else:
			lonLeft = -1*int(westSplit[-1])
			ns = westSplit[0]
		lonRight = lonLeft + 1
		if ns[0] == 'n': latTop = int(ns[1:])
		else: latTop = -1*int(ns[1:])
		latBottom = latTop - 1
		
		pixWE = float(((lon-lonLeft)/(lonRight-lonLeft))*np.shape(terrainArray)[1])
		pixNS = float(((lat-latBottom)/(latTop-latBottom))*np.shape(terrainArray)[0])
		
		if pixWE < 0 or pixWE > np.shape(terrainArray)[1] or pixNS < 0 or pixNS > np.shape(terrainArray)[0]: return None
		else:
			pixWEpor = pixWE - int(pixWE)
			pixNSpor = pixNS - int(pixNS)
			if pixWEpor < 0.5:
				elevWE = ((0.5+pixWEpor)*float(terrainArray[int(pixNS)][int(pixWE)]))+((0.5-pixWEpor)*float(terrainArray[int(pixNS)][int(pixWE)-1]))
				if pixNSpor < 0.5:
					elevFinal = ((0.5+pixNSpor)*elevWE)+((0.5-pixNSpor)*float(terrainArray[int(pixNS)-1][int(pixWE)]))
				else:
					elevFinal = ((1.5-pixNSpor)*elevWE)+((-0.5+pixNSpor)*float(terrainArray[int(pixNS)-1][int(pixWE)]))
			else:
				elevWE = ((1.5-pixWEpor)*float(terrainArray[int(pixNS)][int(pixWE)]))+((-0.5+pixWEpor)*float(terrainArray[int(pixNS)][int(pixWE)-1]))
				if pixNSpor < 0.5:
					elevFinal = ((0.5+pixNSpor)*elevWE)+((0.5-pixNSpor)*float(terrainArray[int(pixNS)-1][int(pixWE)]))
				else:
					elevFinal = ((1.5-pixNSpor)*elevWE)+((-0.5+pixNSpor)*float(terrainArray[int(pixNS)-1][int(pixWE)]))
			print(elevFinal)
			return elevFinal

def getRiverPointElevations(riverWays):
	finalRivers = []
	for i in range(len(riverWays)):
		way = riverWays[i]
		finalRiver = []
		nodes = way.get_nodes(resolve_missing=True)
		for node in nodes: finalRiver.append([float(node.lat), float(node.lon), getElevation(node.lat, node.lon)])
		print((str(i)+'/'+str(len(riverWays))), finalRiver[-1], finalRiver[0])
		if finalRiver[-1][2] != None and finalRiver[0][2] != None and finalRiver[-1][2] > finalRiver[0][2]: finalRiver.reverse()
		finalRivers.append(finalRiver)
	return finalRivers

print("Downloading river data...")
result = api.query("""way["waterway"](40.76,-123.155,40.792,-123.1);out;""")
print("Finished downloading.")

riverWays = result.ways
finalRivers = getRiverPointElevations(riverWays)

ponds = []
for river in finalRivers:
	stepRiver = list(reversed(river))
	currentHigh = 0
	inaPond = False
	tempPond = []
	for i in range(0, len(stepRiver)-1):
		if stepRiver[i][2] == None or stepRiver[i][2] > currentHigh:
			if inaPond == True:
				ponds.append(tempPond)
				tempPond = []
			inaPond = False
			currentHigh = stepRiver[i][2]
		else:
			inaPond = True
			tempPond.append([stepRiver[i][0],stepRiver[i][1]])
			

print(ponds)