from math import *

def areaOfCircle(r):
	return r**2*pi

def areaOfPi(r, a):
	return areaOfCircle(r) * a / (2 * pi)

def opCordOnCircle(x, r):
	return sqrt(r ** 2 - x ** 2)

def areaOfIntersection(r, a, b, c, d):
	if b[1] < opCordOnCircle(b[0], r): return (c[0] - d[0]) * (a[1] - d[1])
	elif d[1] >= opCordOnCircle(d[0], r): return 0

	if a[1] < opCordOnCircle(a[0], r) and c[1] < opCordOnCircle(c[0], r):
		left = opCordOnCircle(a[1], r)
		right = c[0]
	elif a[1] < opCordOnCircle(a[0], r) and c[1] >= opCordOnCircle(c[0], r):
		left = opCordOnCircle(a[1], r)
		right = opCordOnCircle(d[1], r)
	elif a[1] >= opCordOnCircle(a[0], r) and c[1] < opCordOnCircle(c[0], r):
		left = a[0]
		right = c[0]
	elif d[1] < opCordOnCircle(d[0], r):
		left = a[0]
		right = opCordOnCircle(d[1], r)
		
	areaOfBottom = (right-left) * c[1]
	areaOfLeft = (left - a[0]) * (a[1] - d[1])
	return areaOfPoleOnQuarter(r, left, right) - areaOfBottom + areaOfLeft

def areaOfPoleOnQuarter(r, left, right):
	angleB = acos(right/r)
	angleA = acos(left/r) - angleB

	areaOfPiA = areaOfPi(r, angleA)
	areaOfTriAB = opCordOnCircle(left, r) * left / 2
	areaOfTriB = (opCordOnCircle(right, r) * left / right) * left / 2

	areaOfUpper = areaOfPiA - (areaOfTriAB - areaOfTriB)
	areaOfBottom = max(opCordOnCircle(right, r) * right / 2 - areaOfTriB, 0)

	return areaOfUpper + areaOfBottom

def areaOfDeadZoneWithString(input, n):
	R = input["safeR"]

	center = n * input["distString"]
	left = max(min(R, center - input["deadString"]), 0)
	right = min(R, center + input["deadString"])
	result = areaOfPoleOnQuarter(R, left, right)

	divider = n==0 and 1 or 2
	for i in range(1, input["numStrings"] + 2):
		center = input["distString"] * i
		top = center + input["deadString"]
		bottom = center - input["deadString"]
		result -= areaOfIntersection(R, [left, top], [right, top], [right, bottom], [left, bottom])/divider

	return result

def main():
	import sys
	numberOfInputs = int(sys.stdin.readline())
	for i in range(1, numberOfInputs+1):
		rawInput = map(lambda a:float(a), sys.stdin.readline().split())
		input = {"f":rawInput[0], "R":rawInput[1], "t":rawInput[2], "r":rawInput[3],"g":rawInput[4]}

		input["inRingR"] = input["R"] - input["t"]
		input["safeR"] = input["inRingR"] - input["f"]
		input["distString"] = input["g"] + input["r"] * 2
		input["deadString"] = input["r"] + input["f"]

		input["numStrings"] = int(input["inRingR"] / input["distString"])
		areaOfQuarter = areaOfCircle(input["R"]) / 4
		areaOfFlyDeadRing = areaOfQuarter - areaOfCircle(input["safeR"]) / 4

		areasOfDeadZone = map(lambda a: areaOfDeadZoneWithString(input, a), range(input["numStrings"]+1))
		areaOfDeadZone = sum(areasOfDeadZone)
		areaOfDeadZone *= 2
		areaOfDeadZone -= input["deadString"] ** 2

		result = min(1, round((areaOfDeadZone + areaOfFlyDeadRing) / areaOfQuarter,6))
		print "Case #"+str(i)+": " + ("%(#).06f" % {"#":result})#  + " " + str(rawInput)

if __name__ == "__main__": main()
