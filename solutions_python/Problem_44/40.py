#infile = open('/home/patanjali/Desktop/B-small-attempt0(2).in')
infile = open('/home/patanjali/Desktop/B-large.in')
#outfile = open('/home/patanjali/codejam/B-small.out','w')
outfile = open('/home/patanjali/codejam/B-large.out','w')

import math

num_cases = int(infile.readline().strip())

for case_no in xrange(1,num_cases+1,1):
	num_flies = int(infile.readline().strip())
	## Getting the coords and velocity of the center of mass.
	coords = [0,0,0,0,0,0]
	for fly_no in xrange(num_flies):
		line = infile.readline().strip().split(" ")
		for i in xrange(6):
			coords[i] += int(line[i])
	coords = [x/(num_flies*1.0) for x in coords]
	try:
		tmin = -1*(coords[0]*coords[3] + coords[1]*coords[4] + coords[2]*coords[5])/(coords[3]*coords[3] + coords[4]*coords[4] + coords[5]*coords[5]*1.0)
	except:
		tmin = -1
	if tmin < 0:
		minvals = math.sqrt(coords[0]*coords[0] + coords[1]*coords[1] + coords[2]*coords[2]) , 0
	else:
		xmin = coords[0] + coords[3]*tmin
		ymin = coords[1] + coords[4]*tmin
		zmin = coords[2] + coords[5]*tmin
		minvals = math.sqrt(xmin*xmin + ymin*ymin + zmin*zmin) , tmin
	outfile.write("Case #%s: %s %s\n" %(case_no, minvals[0], minvals[1]))

infile.close()
outfile.close()
