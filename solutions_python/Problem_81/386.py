import math
from decimal import Decimal


#infile = open("A-large-practice.in","r")
#infile = open("input.txt","r")
infile = open("A-large.in","r")
firstr = 0
case = 1
records = infile.readlines()
infile.close()


i = 0
while i < len(records):
	#print records[i]
	if i == 0:
		i = i + 1
		continue
	records[i] = records[i].replace("\n","")
	n = int(records[i])
	i = i + 1
	teams = []
	for j in range(0,n):
		records[i] = records[i].replace("\n","")
		teams.append(records[i])
		i = i+1
		#print teams[j]
	wp = []
	played = []
	won = []
	for k in range(0,n):
		contp = 0
		contw = 0
		for j in range(0,n):
			if teams[k][j] != '.':
				contp = contp + 1
			if teams[k][j] == '1':
				contw = contw + 1
		played.append(contp)
		won.append(contw)
		
	for k in range(0,n):
		wp.append(float(won[k])/float(played[k]))
	owp = []
	for k in range(0,n):
		averowp = 0
		for j in range(0,n):
			if teams[k][j] != '.':
				wpc = wp[j]
				if teams[k][j] == '1':
					owpc = float(won[j]) / float(played[j] -1)
				else:
					owpc = float(won[j]-1) / float(played[j] -1)
				averowp = averowp + owpc
		owp.append(float(averowp)/float(played[k]))
	oowp = []
	for k in range(0,n):
		averoowp = 0
		for j in range(0,n):
			if teams[k][j] != '.':
				averoowp = averoowp + owp[j]
		oowp.append(float(averoowp)/float(played[k]))
	print "Case #"+ str(case)+":"
	for k in range(0,n):
		rpi = 0.25 * wp[k] + 0.50 * owp[k] + 0.25*oowp[k]
		print str(rpi)
	case = case + 1
	#i = i + 1
	
		
