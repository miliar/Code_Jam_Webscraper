
f = open("A-large.in", "r")
c = 0

for line in f:
	p = line.split(" ")
	if len(p) == 1:
		continue;
	c += 1
	n = int(p[0])
	k = int(p[1])
	
	if (k + 1) % (2 ** n) == 0:
		print "Case #%d: ON" % c
	else:
		print "Case #%d: OFF" % c

f.close()