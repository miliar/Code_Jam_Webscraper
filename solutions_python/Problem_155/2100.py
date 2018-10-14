#!/usr/bin/env python

ifname = 'A-large.in'
ofname = 'A-large.out'
outf = open(ofname, 'w')
inf = open(ifname)

lines = [line.strip() for line in inf]
inf.close()

T = int(lines[0])

for i in range(1,len(lines)):
	data = lines[i].split()
	smax = int(data[0])
	sdat = [int(val) for val in data[1]]
	inv = 0
	standing = 0
	for si in range(len(sdat)):
		if standing < si:
			#print 'Case #{0}: have {1} need {2} inviting {3}'.format(i,standing,si,si-standing)
			inv += si - standing
			standing += si - standing
		standing += sdat[si]
	outf.write('Case #{0}: {1}\n'.format(i, inv))
		
outf.close()