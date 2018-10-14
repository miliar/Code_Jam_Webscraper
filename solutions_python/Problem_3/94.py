#!/usr/bin/python
import sys, psyco, math
psyco.full()

def frange(fr, to, step):
	off = fr
	while off<to:
		yield off
		off += step

def getGrid( f, R, t, r, g ):
	grid = []
	innerRadius = R-t-f
	lbCorner = lambda n,m: ( (2*n+1)*r+n*g+f, (2*m+1)*r+m*g+f )

	for x in frange(r+f, innerRadius, 2*r+g):
		for y in frange(r+f, innerRadius, 2*r+g):
			grid.append( (x,y) )

	return grid

def getArea( x, y, p1_x, p1_y, p2_x, p2_y, winSize, innerRadius ):
	A1 = (p1_x - x) * (p2_y - y )
	A2 = (p2_x-p1_x)* (p2_y - y )
	A3 = (p1_x - x) * (p1_y - p2_y )
	A4 = (p2_x-p1_x)* (p1_y - p2_y ) / 2
	a = math.sqrt( ( p2_x-p1_x )**2 + ( p1_y-p2_y )**2 ) / 2
	teta = 2*math.asin(a/innerRadius)
	A5 = 0.5 * innerRadius**2 * (teta - math.sin(teta))
	#print A1, A2, A3, A4, A5
	return A1+A2+A3+A4+A5

def solve( f, R, t, r, g ):
	freeArea = 0.0
	innerRadius = R-t-f
	winSize = g-2*f
	#get grid point coordinates
	grid = getGrid( f, R, t, r, g )
	
	inCircle = lambda x,y: x**2 + y**2 <= innerRadius**2

	#iterate the quadrats of the grid 
	for (x,y) in grid:
		if not inCircle(x,y): continue
		if inCircle( x+winSize, y+winSize ):
			freeArea += winSize**2
		else:
			#get intersection points
			if inCircle( x, y+winSize ):
				# 1 3
				p1_y = y+winSize
				p1_x = math.sqrt( innerRadius**2 - p1_y**2 )
				if inCircle( x+winSize, y ):
					# 1
					p2_x = x+winSize
					p2_y = math.sqrt( innerRadius**2 - p2_x**2 )
				else:
					# 3
					p2_y = y
					p2_x = math.sqrt( innerRadius**2 - p2_y**2 )
			else: 
				# 2 4
				p1_x = x
				p1_y = math.sqrt( innerRadius**2 - p1_x**2 )
				if inCircle( x+winSize, y ):
					# 2
					p2_x = x+winSize
					p2_y = math.sqrt( innerRadius**2 - p2_x**2 )
				else:
					# 4
					p2_y = y
					p2_x = math.sqrt( innerRadius**2 - p2_y**2 )

			#print p1_x, p1_y, p2_x, p2_y

			#get area of quadrat
			A = getArea( x, y, p1_x, p1_y, p2_x, p2_y, winSize, innerRadius )

			#add area
			freeArea += A
	
	quartCircle = ( math.pi * R**2 ) / 4

	P = 1 - freeArea/quartCircle
	return P


first = True
N = -1
case = 1

for line in open(sys.argv[1]):
	line = line[:-1]
	
	if first:
		N = int(line)
		first = False
		continue

	if case <= N:
		f, R, t, r, g = [ float(x) for x in line.split() ]
		P = solve( f, R, t, r, g )
		print "Case #%d: %.6f" % (case, P)
		case += 1
