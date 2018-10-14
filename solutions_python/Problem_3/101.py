# Google CodeJam 2008
# Qualification round - problem 1
# autor: HighEgg
import sys
from math import *

# calculates the area of the set of all points inside disk of radius R that lie
# upper right from a point (x,y)
def upleft(x,y,R):
    if x < R and y < R:
	a = R*R*(acos(x/R) - asin(y/R)) 
	if a <= 0:
	    return 0
	else:
	    a += -y*sqrt(R*R-y*y) - x*sqrt(R*R-x*x) + 2*x*y
	    return a/2
    else:
	return 0

# calculates the area of the portion of a square lx,ly,lx+a,ly+a
# that lies inside a disk of radius R
def sqarea(lx,ly,a,R):
    if lx >= R or ly >= R:
	return 0
    ux = lx + a
    uy = ly + a
    if lx*lx + ly*ly >= R*R:
	return 0
    elif ux*ux + uy*uy <= R*R:
	# the simple case
	return a*a
    else:
	return upleft(lx,ly,R) - upleft(ux,ly,R) - upleft(lx,uy,R) + upleft(ux,uy,R)


def freearea(f,R,t,r,g):
    N = int(ceil((R+g)/(2*r+g)))
    a = g-2*f
    if a <= 0:
	return 0
    area = 0
    for i in range(N):
	for j in range(N):
	    area += sqarea(r+f+(2*r+g)*i,r+f+(2*r+g)*j,a,R-t-f)
    return area

input = open(sys.argv[1],'r')
ncases = int(input.readline())

for icase in range(ncases):
    icase += 1
    f,R,t,r,g = map(float,input.readline().split())
    print "Case #%d: %8.6f" % (icase,1-4*freearea(f,R,t,r,g)/(pi*R*R))
