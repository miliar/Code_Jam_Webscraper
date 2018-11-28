#!/usr/bin/python3

import math
from decimal import Decimal

t = int(input());
for ti in range (1, t+1):
	n,k  = [int(s) for s in input().strip().split(" ")] 
	
	pancakes = []
	while n>0:
		pancakes.append([int(s) for s in input().strip().split(" ")]);
		pancakes[-1].append(2*pancakes[-1][0]*pancakes[-1][1]);
		n -= 1;
	
	pancakes = sorted(pancakes, key=lambda p: (-p[0], -p[1]));
	#print(pancakes);
	
	
	maxarea = 0;
	
	for i in range(0, len(pancakes)):
		area = pancakes[i][0]*pancakes[i][0] + pancakes[i][2];
		
		others = sorted(pancakes[i+1:], key=lambda p: (-p[2]))
		
		area += sum(z for (x, y, z) in others[0:k-1]);
		
		if area > maxarea:
			maxarea = area;
	
	
	
	
	
	
	
	print("Case #{}: {}".format(ti, maxarea*Decimal("3.14159265358979323846264338327950288419716939937510582097494459230")));
