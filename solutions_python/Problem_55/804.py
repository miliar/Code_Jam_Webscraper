#!/usr/bin/python

fp = open("C-small-attempt0.in", "r")
T = int(fp.readline())
for i in range(T):
	line = fp.readline()
	line = line.strip()
	x = line.split()
	R = int(x[0])
	k = int(x[1])
	N = int(x[2])
	line = fp.readline()
	line = line.strip()
	x = line.split()
	g = []
	for j in range(N):
		g.insert(0, int(x[j]))
	grand_total = 0
	for j in range(R):
		total = 0
		count = 0
		while(total < k):
			if(count == N):
				break;
			if(g[-1] + total > k):
				break;
			else:
				ink = g.pop()
				total += ink
				g.insert(0, ink)
				count += 1
		grand_total += total
	string = "Case #"+ str(i+1) +": "+str(grand_total)
	print string
