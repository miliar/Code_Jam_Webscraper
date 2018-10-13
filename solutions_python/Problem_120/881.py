import random
import math

def run():
	with open('input') as f:
	    w = [int(x) for x in f.readline().split()][0] # read first line
	    for i in range(1, (w+1)):
	    	r, t = [int(x) for x in f.readline().split()]
	    	count = solve(2, 2*r-1, -1 * t)
	    	count = math.ceil(count)
	    	while (True):
	    		if (check(count, r, t)):
	    			print 'Case #'+str(i)+": " + str(count)[:-2]
	    			break
    			count = count - 1

def check(B, r, t):
	sol = 2 * B * B + B * (2 * r - 1) - t
	if sol <= 0:
		return True;
	else:
		return False;

def solve(a, b, c):
	return (-1 * b + math.sqrt(b * b - 4 * a * c))/(2 * a)

run();