import math,sys,os,time

def dance(l):
	dancers = int(l.split()[0])
	suprises = int(l.split()[1])
	threshold = int(l.split()[2])
	scores = l.split()[3:]

	count = 0

	for score in scores:
		score = int(score)
		if db[score] >= threshold:
			count += 1
			continue
		if suprises > 0:
			if sb[score]>db[score]:
				if sb[score]>=threshold:
					count +=1
					suprises -=1
					continue

	return count	

db = [0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
sb = [0,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,10,10]

file = open(sys.argv[1],'r')

for i in range(int(file.readline())):
	print "Case #" + str(i+1) + ":\t" + str(dance(file.readline()))
