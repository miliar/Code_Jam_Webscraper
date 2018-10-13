#!/usr/bin/python2
import sys, os

fn = "myfile"
if len(sys.argv) == 2:
	if os.path.exists(sys.argv[1]):
		fn = sys.argv[1]

f = open(fn,"r")

cases = f.readline();

cc = 0;

pp = {}
for yyy in range(1,10):
	pp[yyy] = 10**(yyy-1)

for line in f:
	cc += 1
	p = line.strip().split(" ")
	f = p[0]
	t = p[1]
	ff = int(f)
	tt = int(t)
	c = 0;
	for x in range(ff,tt+1):
		xx = str(x);
		d = {}
		for y in range(1,len(xx)):
			z = xx[y:]
			zl = len(z)
			if int(z) >= pp[zl]:
				zz = z + xx[:-zl]
				zzz = int(zz)
				if zzz > x and zzz <= tt: 
					if zzz not in d:
						d[zzz] = 1
						c += 1

	print "Case #"+str(cc)+": "+str(c)
