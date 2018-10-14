import string
import re
import random

dataIn = []

fp = open('1small.txt', 'r')
dataIn = fp.read().splitlines()
fp.close()
text_file = open('1output.txt','w')

for i in range(len(dataIn)):
	point = 0
	need = 0
	if i == 0:
		testMax = int(dataIn[i])
	else:
		dataIn[i].split(' ')
		for x in range(2,int(dataIn[i][0])+3):
			if x == 2:
				point += int(dataIn[i][x])
			else:
				if int(dataIn[i][x]) != 0:
					if x-2 > point:
						need += (x-2)-point
						point += (x-2)-point
					point += int(dataIn[i][x])
		text_file.write("Case #{}: {}\n".format(i,need))
text_file.close()

'''
for i in range(len(dataIn)):
	with open('1output.txt','w') as tf:
		for i in range(len(dataIn)):
			tf.write(dataIn[i][0])
'''