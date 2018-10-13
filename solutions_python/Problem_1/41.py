#!/usr/bin/python

case = "large"
input_file = "A-%s.in" % case
output_file = "A-%s.out" % case

fin = open(input_file)
fout = open(output_file, "w")

n = int(fin.readline().strip())
#print n

for z in xrange(n):
	s = int(fin.readline().strip())
	#print s
	eng = [fin.readline() for i in xrange(s)]
	#print eng
	q = int(fin.readline().strip())
	#print q
	quer = [fin.readline() for i in xrange(q)]
	#print quer
	t = [0] * s
	for x in xrange(q-1, -1, -1):
		#print "it", x
		sw = min([t[i] for i in range(s) if eng[i] != quer[x]]) + 1
		#print sw
		tt = [0] * s
		for i in range(s):
			if eng[i] == quer[x]:
				tt[i] = sw
			else:
				tt[i] = min(sw, t[i])
		t = tt
		#print t
	res = min(t)
	print >> fout, "Case #%d:" % (z+1), res

fin.close()
fout.close()
