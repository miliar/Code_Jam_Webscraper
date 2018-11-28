import sys
import math

def GetBox(f, R, r, g, i, j):
	b = r + g / 2
	halfWidth = g / 2 - f
	pitch = g + 2 * r
	x = b + pitch * i
	y = b + pitch * j
	box = x - halfWidth, y - halfWidth, x + halfWidth, y + halfWidth
	return box
	
def GetBoxList(f, R, t, r, g):
	boxList = []
	n = int((R - t - f + g + 2 * r) / (g + 2 * r))
	for i in range(n):
		for j in range(n):
			box = GetBox(f, R, r, g, i, j)
			boxList.append(box)
	return boxList

def CalculateArcArea(realR, len):
	a = math.asin((len / 2) / realR)
	h = realR * math.cos(a)
	bigArea = (math.pi * (realR ** 2)) * a / math.pi
	smallArea = len * h / 2
	return bigArea - smallArea
	
def CalculateAreaA(realR, box):
	x1 = box[0]
	x2 = box[2]
	h = x2 - x1
	y1 = math.sqrt(realR ** 2 - x1 ** 2)
	y2 = math.sqrt(realR ** 2 - x2 ** 2)
	a = y1 - box[1]
	b = y2 - box[1]
	len = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
	
	area = (a + b) * h / 2
	return area + CalculateArcArea(realR, len)

def CalculateAreaB(realR, box):
	x1 = box[0]
	y1 = math.sqrt(realR ** 2 - x1 ** 2)
	y2 = box[1]
	x2 = math.sqrt(realR ** 2 - y2 ** 2)
	len = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
	area = (y1 - y2) * (x2 - x1) / 2
	area2 = CalculateArcArea(realR, len)
	return area + area2


def CalculateAreaC(realR, box):
	y1 = box[3]
	x1 = math.sqrt(realR ** 2 - y1 ** 2)
	x2 = box[2]
	y2 = math.sqrt(realR ** 2 - x2 ** 2)
	len = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
	area = ((box[2] - box[0]) ** 2) - (box[2] - x1) * (box[3] - y2) / 2
	return area + CalculateArcArea(realR, len)

def CalculateAreaD(realR, box):
	y1 = box[3]
	x1 = math.sqrt(realR ** 2 - y1 ** 2)
	y2 = box[1]
	x2 = math.sqrt(realR ** 2 - y2 ** 2)
	len = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
	h = box[3] - box[1]
	a = x1 - box[0]
	b = x2 - box[0]
	area = (a + b) * h / 2
	return area + CalculateArcArea(realR, len)

def CalculateArea(realR, box):
	minR = math.sqrt(box[0] ** 2 + box[1] ** 2)
	maxR = math.sqrt(box[2] ** 2 + box[3] ** 2)
	aR = math.sqrt(box[0] ** 2 + box[3] ** 2)
	bR = math.sqrt(box[1] ** 2 + box[2] ** 2)
	
	if maxR <= realR:
		# In
		return (box[2] - box[0]) * (box[3] - box[1])
	elif minR >= realR:
		# Out 
		return 0
	elif (aR >= realR and bR <= realR):
		# A
		return CalculateAreaA(realR, box)
	elif (aR >= realR and bR >= realR):
		# B
		return CalculateAreaB(realR, box)
	elif (aR <= realR and bR <= realR):
		# C
		return CalculateAreaC(realR, box)
	elif (aR <= realR and bR >= realR):
		# D
		return CalculateAreaD(realR, box)

def CalculateProbability(f, R, t, r, g):
	if g - 2 * f < 0:
		return 0

	if R - t - f < 0:
		return 0

	boxList = GetBoxList(f, R, t, r, g)	
	area = 0
	realR = R - t - f
	for box in boxList:
		area += CalculateArea(realR, box)
	return 1 - area * 4 / (math.pi * (R ** 2))

def main():
	
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	
	ifd = open(input_file, 'r')
	ofd = open(output_file, 'w')
	
	N = int(ifd.readline())
	
	for n in range(N):
		line = ifd.readline()
		params = line.split()
		
		f = float(params[0])
		R = float(params[1])
		t = float(params[2])
		r = float(params[3])
		g = float(params[4])
		
		p = CalculateProbability(f, R, t, r, g)
		
		print n + 1, f, r, t, r, g, "%6f" % p	
		ofd.write("Case #%d: %6f\n" % (n + 1, p))
	ifd.close()
	ofd.close()
	
def main2():
	params = sys.argv
	f = float(params[1])
	R = float(params[2])
	t = float(params[3])
	r = float(params[4])
	g = float(params[5])
	
	p = CalculateProbability(f, R, t, r, g)
		
	print f, r, t, r, g, "%6f" % p	
main()