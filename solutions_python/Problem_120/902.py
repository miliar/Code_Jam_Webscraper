import math
#Equations: 1 mili = (pi)cm^2

#calculate each circle by subtracting the inner circles radius
def calculatebullseye(radius, milliliters):
	numCircles = 0
	while canPaintCircle(getArea(radius + 1), milliliters):
		milliliters -= getArea(radius + 1)
		radius += 2
		numCircles += 1
	print('Mili Left: ' + str(milliliters))
	return numCircles


def getArea(radius):
	return (radius**2) - ((radius - 1)**2)

def canPaintCircle(area, miliRemain):
	return miliRemain >= area


def readInputFile(fileName):
	out = open('ouput.txt', 'w+')
	inp = open(fileName, 'r')
	#first is number of cases
	cases = inp.readline()
	for i in range(int(cases)):
		case = inp.readline()
		radius = int(case.split()[0])
		milliliters = int(case.split()[1])
		print(str(radius) + ' ' + str(milliliters))
		i += 1
		out.write("Case #{0}: {1}\n".format(i, calculatebullseye(radius, milliliters)))

readInputFile('test1.in')