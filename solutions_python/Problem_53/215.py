#!python

f = open("A-large.in")

for i,line in enumerate(f):
	if i == 0:
		continue
	n,k = (int(x) for x in line.split())
	if (k+1)%(2**n) == 0:
		result = "ON"
	else:
		result = "OFF"
	print "Case #%d: %s" % (i,result)