#!/usr/bin/env python3

ip=open("A2.in",'r')

no = ip.readline()
no = int(no)
case_no = 0;
for line in ip:
	#print line
	case_no+=1
	line = line.split(' ',1)
	smax = int(line[0])
	shy = line[1]
	#print smax
	minf = 0
	count = int(shy[0])
	for i in range(1,smax+1):
		x=int(shy[i])
		if(count<i):
			extraf=i-count
			count+=extraf
			minf+=extraf
		count+=x
	print "Case #" + str(case_no) + ": " + str(minf)
