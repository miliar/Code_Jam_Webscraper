#!/usr/bin/python3

import math

def do_case():
	n, p  = [int(s) for s in input().strip().split(" ")]
	groups = [int(s) for s in input().strip().split(" ")]
	g = [0]*p
	for a in groups:
		g[a%p] += 1;
	
	fresh = g[0];
	g[0] = 0;
	if p==2:
		fresh += int(g[1]/2)
		g[1] -= 2*int(g[1]/2)
	elif p==3:
		new = min(g[1], g[2])
		fresh += new
		g[1] -= new
		g[2] -= new
		
		fresh += int(g[1]/3)
		g[1] -= 3*int(g[1]/3)
		fresh += int(g[2]/3)
		g[2] -= 3*int(g[2]/3)
		
	elif p==4:
		new = min(g[1], g[3])
		fresh += new
		g[1] -= new
		g[3] -= new
		
		new = int(g[2]/2)
		fresh += new
		g[2] -= 2*new
		
		j = 2;
		
		new = min(g[2], int(g[3]/2))
		fresh += new
		g[2] -= new
		g[3] -= 2*new
		
		new = min(int(g[1]/2), g[2])
		fresh += new
		g[1] -= 2*new
		g[2] -= new
		
		fresh += int(g[1]/4) + int(g[3]/4)
		g[1] -= 4*int(g[1]/4)
		g[3] -= 4*int(g[3]/4)
	
	if sum(g) > 0:
		fresh += 1 #(first group also gets fresh)
	return fresh;

	
	

t = int(input());
for ti in range (1, t+1):
	print("Case #{}: {}".format(ti, do_case()));
	
 
