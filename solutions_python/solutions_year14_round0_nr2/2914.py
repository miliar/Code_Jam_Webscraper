#!/usr/bin/env python
from sys import *
import math

def farms_time(C, F, N):
	return sum([C/(2+(x-1)*F) for x in xrange(1, N + 1)])

def solve(lines):
	line = lines[0].split(' ')
	base_rate = 2
	C = float(line[0])
	F = float(line[1])
	X = float(line[2])
		
	max_time = X / base_rate
	
	aproximate_farms = int(math.ceil(X / C))
	min_aproximate = max(aproximate_farms - 10, 1)
	
	possiple_times = [farms_time(C, F, x) + X/(2+x*F) for x in range(min_aproximate, aproximate_farms + 10 + 1)]
	
	min_time = min(possiple_times)
	
	return min(min_time, max_time)

def read(counter):
	return [stdin.readline().strip("\n") for x in range(counter)]

def main():
	counter = int(stdin.readline())
	for x in range(counter):
		print("Case #" + str(x + 1) + ": " + str(solve(read(1))))

if __name__ == "__main__":
	main()
