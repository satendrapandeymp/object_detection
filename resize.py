import cv2, os
from glob import glob

imageFolder = raw_input("Give the location of Image folder : ")
factor = raw_input("Give the factor Like 0.5 by which you want to reduce your Image : ")

try:
	factor = float(factor)
except:
	factor = raw_input("Give the number between 0-1 : ")
	factor = float(factor)

imageList = glob(imageFolder + "/*.*")

for path in imageList:                                                          
        img = cv2.imread(path)
	result = cv2.resize(img, None, fx=factor, fy=factor, interpolation=cv2.INTER_CUBIC)
	pathBak = path.split(".")[0] + "_bak." + path.split(".")[1] 
	os.rename(path, pathBak)
	cv2.imwrite(path, result)

print "resized all files in dir : " + imageFolder

