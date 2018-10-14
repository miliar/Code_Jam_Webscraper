#! /usr/bin/env python

from numpy import array
from math import hypot, acos, pi, sqrt, sin

def invertices(center, side, radius):
	out = 0
	points = []
	points.append(array((center[0] - side/2.0, center[1] - side/2.0)))
	points.append(array((center[0] - side/2.0, center[1] + side/2.0)))
	points.append(array((center[0] + side/2.0, center[1] - side/2.0)))
	points.append(array((center[0] + side/2.0, center[1] + side/2.0)))
	for point in points:
		if hypot(point[0], point[1]) <= radius:
			out += 1
	return out, points

def delarea(lenab, radius):
	theta = acos(1.0-((lenab/radius)**2)/2.0)
	return radius**2 * (theta - sin(theta)) / 2.0

def case(infile):
	l = infile.readline().strip().split()
	f, R, t, r, g = map(float, l)
	#print f, R, t, r, g
	t = t + f
	r = r + f
	g = g - 2.0*f
	f = 0.0
	d = g + 2.0*r
	#print f, R, t, r, g
	center = array((d/2.0, d/2.0))
	centers = []
	casedistr = [0,0,0,0,0]
	area = 0.0
	m, n = 0, 0
	#print 'range :', R/d+1
	for n in xrange(int(R/d)+2):
		for m in xrange(int(R/d)+2):
			center[0], center[1] = d*(m+0.5), d*(n+0.5)
			centers.append(center.copy())
			inv, points = invertices(center, g, R-t)
			areap = 0.0
			if inv == 0:
				break
			elif inv == 4:
				areap = g*g
			elif inv == 3:
				a = array([sqrt((R-t)**2 - (points[3][1])**2), points[3][1]])
				b = array([points[3][0], sqrt((R-t)**2 - points[3][0]**2)])
				lenab = hypot(a[0]-b[0], a[1]-b[1])
				#print 'lenab ', lenab, R-t
				areap += delarea(lenab, R-t)
				areap += (b[1]-points[2][1])*g + ((a[0]+b[0])/2.0-points[0][0])*(points[3][1]-b[1])
			elif inv == 2:
				if points[3][1] > points[3][0]: # above 45 degree line
					a = array([points[0][0], sqrt((R-t)**2 - points[0][0]**2)])
					b = array([points[3][0], sqrt((R-t)**2 - points[3][0]**2)])
					lenab = hypot(a[0]-b[0], a[1]-b[1])
					#print 'lenab ', lenab, R-t
					areap += delarea(lenab, R-t)
					areap += g*((a[1]+b[1])/2.0-points[0][1])
				else:
					a = array([sqrt((R-t)**2 - points[3][1]**2), points[3][1]])
					b = array([sqrt((R-t)**2 - points[0][1]**2), points[0][1]])
					lenab = hypot(a[0]-b[0], a[1]-b[1])
					areap += delarea(lenab, R-t)
					areap += g*((a[0]+b[0])/2.0-points[0][0])
			elif inv == 1:
				a = array((points[0][0], sqrt((R-t)**2 - (points[0][0])**2)))
				b = array([sqrt((R-t)**2-points[0][1]**2), points[0][1]])
				lenab = hypot(a[0]-b[0], a[1]-b[1])
				areap += delarea(lenab, R-t)
				areap += (b[0]-points[0][0]) * (a[1]-points[0][1]) / 2.0
			#print m, n, '\t', inv
			#print inv, 
			casedistr[inv] += 1
			area += areap
		inv, points = invertices(center, g, R-t)
		#print 
		if inv == 0:
			pass #break
	p = 1.0 - 4.0 * area / (pi * (R**2))
	#print casedistr
	#from pylab import *
	#plot(array(centers)[:,0], array(centers)[:,1], '.-')
	#show()
	return p

if __name__ == '__main__':
	infile = open('C-small-attempt0.in')
	N = int(infile.readline())
	for casenum in xrange(N):
		p = case(infile)
		print 'Case #%d: %f' %(casenum+1, p)
	

