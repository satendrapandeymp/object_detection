import pandas as pd
import os

# Reading FIle
fileName = raw_input("Give your .csv Filename for sample try train_labels.csv : ")
data = pd.read_csv(fileName)


# Doing operation as you want
# Like I'm just diving each element of csv by 3
for col in data.columns:
	# you can also do it like data[col] /= 3 :p below code is just for complex scenario
	arr = []
	flag = 0
        for i in data[col]:
	    try:
            	arr.append(int(i/3))
	    except:
	    	flag = 1
	    	break
	if flag == 0:
        	data[col] = arr


# Make backup of original file
bakPath = fileName.split(".")[0] + "_bak." + fileName.split(".")[1]
os.rename(fileName, bakPath)


# To save that as .csv file
test = pd.DataFrame(data) 
test.to_csv(fileName) 
