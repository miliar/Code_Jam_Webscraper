import csv
import os

ifile = open(os.path.expanduser('~/Desktop/B-small-attempt0.in'), "rU")
reader = csv.reader(ifile)

ofile = open(os.path.expanduser('~/Desktop/problem1.out'), "wb")
writer = csv.writer(ofile)

f = open('cookieoutput.out', 'r+')

def calcCookies(X, C, F):
	opt = float("inf")
	numFarms = 0
	while(1):
		val = float(X)/(2 + numFarms*F)
		for i in range (0, numFarms):
			val += float(C)/(2 + i*F)
		if val >= opt:
			numFarms-=1
			break
		opt = val
		numFarms+=1
	return opt


rownum = 0
case = 0
C = 0
F = 0
X = 0
for row in reader:
	if (rownum == 0):
		cases = int(row[0])
	else:
		C = float(row[0].split()[0])
		print(C)
		F = float(row[0].split()[1])
		print(F)
		X = float(row[0].split()[2])
		print(X)
		optTime = calcCookies(X, C, F)
		case = case + 1
		f.write("Case #" + `case` + ": " + `optTime` + "\n")
	rownum+=1
	


