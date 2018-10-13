#!/usr/bin/python
from math import sqrt

def is_square(num):
	if(num ==1):
		return True
  	x = num // 2
  	seen = set([x])
  	while x * x != num:
    		x = (x + (num // x)) // 2
    		if x in seen: 
			return False
    		seen.add(x)
  	return True

def is_pal(num):
	S = str(num)
	S = list(S)
	S.reverse()
	S = int("".join(S))
	if(S == num):
		return True
	return False
	
T = int(raw_input().strip())
for i in range(1, T+1):
	L, P = raw_input().strip().split(" ")
	L = int(L)
	P = int(P)
	count = 0
	for N in range(L, P+1):
		if(is_square(N)):
			if(is_pal(N) and is_pal(int(sqrt(N)))):
				count = count+1	
					
	print "Case #" + str(i) + ": " + str(count)
