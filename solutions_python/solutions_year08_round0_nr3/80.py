import sys
from math import *
from random import *

# PIL library (www.pythonware.com/products/pil/)
import Image
import ImageDraw

visualize = False

def getLine():
	global fin
	line = fin.readline()
	if line[-1]=="\n":
		line = line[:-1]
	return line


def rectCircleAreaNumerical(x1,y1,x2,y2,r):
	print "rci: ",x1,y1,x2,y2,r
	n = 10000
	res = 0.0
	for i in range(n):
		x = x1+(x2-x1)*(i+0.5)/n
		if x>=r:
			break
		y = sqrt(r*r-x*x)
		y = max(y1,y)
		y = min(y2,y)
		res += y-y1
	res *= (x2-x1)/n
	print "rci: ",res
	return res


def segmentArea(angle,r):
	return r*r*(0.5*angle-0.5*sin(angle))

def roundTrapezoidArea(x1,x2,y,r):
	return 0.5*(segmentArea(2*acos(x1/r),r)-segmentArea(2*acos(x2/r),r))-\
		(x2-x1)*y

def rectCircleArea(x1,y1,x2,y2,r):
#	print "rci: ",x1,y1,x2,y2,r
	assert x1*x1+y1*y1<=r*r
#	if x1*x1+y1*y1>=r*r:
#		return 0
	if x2*x2+y2*y2<=r*r:
		return (x2-x1)*(y2-y1)

	if x1*x1+y2*y2>r*r:
		if x2*x2+y1*y1>r*r:
			# lower left corner
			xm = sqrt(r*r-y1*y1)
			return roundTrapezoidArea(x1,xm,y1,r)
		else:
			# horizontal fragment
			return roundTrapezoidArea(x1,x2,y1,r)
	else:
		if x2*x2+y1*y1>r*r:
			# vertical fragment
			return roundTrapezoidArea(y1,y2,x1,r)
		else:
			# square with no upper right corner
			xm= sqrt(r*r-y2*y2)
			return (xm-x1)*(y2-y1)+roundTrapezoidArea(xm,x2,y1,r)

def solve(case):

	f,R,t,r,g = map(float,getLine().split(" "))


	if 2*f>=g:
		return "1"

	radius = R-t-f

	size = g-2*f
	step = g+2*r

	start = f+r
	n = int(ceil(radius/step))

	if visualize:
		im = Image.new("RGB",(600,600))
		draw = ImageDraw.Draw(im)
		scale = (im.size[0]-1)/(R+1e-6)
		draw.ellipse((-scale*radius,-scale*radius,scale*radius,scale*radius))
	

	x = start
	j1 = n

	s = 0
	for i in range(n):
		while j1>=0 and x*x+(start+j1*step)**2>=radius*radius:
			j1 -= 1
		if j1<0:
			break
		j2 = j1
		while j2>=0 and (x+size)**2+(start+j2*step+size)**2>=radius*radius:
			j2 -= 1

		s += size*size*(j2+1)

		if visualize:
			for j in range(n,j1,-1):
				y = start+j*step
				draw.rectangle((scale*x,scale*y,scale*(x+size),scale*(y+size)),
								outline=(0,0,150))
			for j in range(j2,-1,-1):
				y = start+j*step
				draw.rectangle((scale*x,scale*y,scale*(x+size),scale*(y+size)),
								outline=(100,100,100))

		for j in range(j1,j2,-1):
			y = start+j*step
			if visualize:
				draw.rectangle((scale*x,scale*y,scale*(x+size),scale*(y+size)))
			s += rectCircleArea(x,y,x+size,y+size,radius)

		j1 = j2+1
		x += step

	if visualize:
		im = im.transpose(Image.FLIP_TOP_BOTTOM)
		im.save("%s.bmp"%case)
	return "%.7f"%(1-s/(0.25*pi*R*R))

#########
if len(sys.argv) != 2:
	print "Specify input file"
	exit(1)

fin = open(sys.argv[1])


n = int(getLine())

fout = open("out","wt")

for i in range(1,n+1):
	print "Solving",i
	fout.write("Case #%s: "%i)
	fout.write(solve(i))
	fout.write("\n")

fout.close()