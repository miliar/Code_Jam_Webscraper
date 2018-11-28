#!/usr/bin/env python

if __name__ == "__main__":
	f = open("A-small.in", "r")
	lines = f.readlines()
	t = int(lines[0])
	for ii in range(t):
		ok = 0
		[n, pd, pg] = lines[ii+1].split()
		(n, pd, pg) =(int(n), int(pd), int(pg))
		for d in range(1, n+1):
			if ( d * pd) % 100 == 0:
				won = (n * pd)/100
				if not ((pd != 0 and pg == 0) or (pd != 100 and pg == 100)):  
					ok = 1
					break;
		if ok:
			print "Case #%s: Possible" %(ii+1)
		else:
			print "Case #%s: Broken" %(ii+1)
