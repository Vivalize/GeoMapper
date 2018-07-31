import json
from osgeo import ogr
import sys
from PIL import Image, ImageDraw
Image.MAX_IMAGE_PIXELS = 1000000000


def getGeoData(dataType):
	woodlandPath = '/Users/Marko/Downloads/WOODLAND_6_California_GU_STATEORTERRITORY/WOODLAND_6_California_GU_STATEORTERRITORY.gdb'
	aquaticPath = '/Users/Marko/Downloads/NHD_H_California_State_GDB/NHD_H_California_State_GDB.gdb'
	
	driver = ogr.GetDriverByName("OpenFileGDB")
	if dataType == 'lakes':
		dataIndex = 27
		dataset = driver.Open(aquaticPath, 0)
	elif dataType == 'creeks':
		dataIndex = 22
		dataset = driver.Open(aquaticPath, 0)
	elif dataType == 'rivers':
		dataIndex = 24
		dataset = driver.Open(aquaticPath, 0)
	else:
		dataIndex = 3
		dataset = driver.Open(woodlandPath, 0)
	allData = []
	for i in range(1,len(dataset[3])):
		try:
			if dataIndex == 22: allData.append(json.loads(dataset[dataIndex][i].ExportToJson())['geometry']['coordinates'][0])
			else: allData.append(json.loads(dataset[dataIndex][i].ExportToJson())['geometry']['coordinates'][0][0])
		except:
			continue
	return allData


		
def graphPolys(allPolys, bounds='Weaverville', color='white', outputName='Output.png', fillType='fill', showProg=False):
	
	if allPolys == 'creeks': fillType = 'lines'
	if isinstance(allPolys, str): allPolys = getGeoData(allPolys)
	
	if bounds == 'Weaverville':
		baseImage = Image.open('Weaverville Blackdrop.png')
		minX = -124
		maxX = -122
		minY = 40
		maxY = 42
	else:
		baseImage = Image.open('blackcali.png')
		minX = -125
		maxX = -114
		minY = 32
		maxY = 43
		
	if color == 'aqua' or color == 'cyan': fillColor = (0,255,255)
	elif color == 'green': fillColor = (0,255,0)
	elif color == 'red': fillColor = (255,0,0)
	elif color == 'blue': fillColor = (0,0,255)
	else: fillColor = (255,255,255)
	
	baseWidth, baseHeight = baseImage.size
	draw = ImageDraw.Draw(baseImage)
	
	for poly in allPolys:
		polyInBounds = False
		for coord in poly:
			if coord[0] > minX and coord[0] < maxX and coord[1] > minY and coord[1] < maxY:
				polyInBounds = True
				
		if polyInBounds:
			fixedPoly = []
			for coord in poly:
				xCoor = int((coord[0]-minX)*baseWidth/(maxX-minX))
				yCoor = baseHeight-int((coord[1]-minY)*baseHeight/(maxY-minY))
				if xCoor < 0: xCoor = 0
				if xCoor > baseWidth: xCoor = baseWidth
				if yCoor < 0: yCoor = 0
				if yCoor > baseHeight: yCoor = baseHeight
				fixedPoly.append((xCoor,yCoor))

			# Draw the poly
			if fillType == 'fill': draw.polygon(fixedPoly, fill=fillColor)
			else: draw.line(fixedPoly, fill=fillColor, width=5)
		
		if i%int(len(dataset[dataIndex])/1000)==0:
			perc = str(i/len(dataset[dataIndex])*100)
			if perc[1] == '.': print(perc[:3]+'%')
			else: print(perc[:4]+'%')
		if i%10000 == 0 and showProg: baseImage.show()
			
	baseImage.show()
	baseImage.save(outputName)
	

			
			