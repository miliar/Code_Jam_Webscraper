#!/usr/bin/env python3.2

def nextTest():
	stuff = input().split()
	C = float(stuff[0]) # cost of a farm
	F = float(stuff[1])
	X = float(stuff[2])
	# for 'current'
	c_rate = 2.0
	c_time = 0.0
	# Simulates the next time I can buy a farm
	while True:
		c_time += C / c_rate
		if (X - C) / c_rate < X / (c_rate + F): # not buying
			break
		# buying
		c_rate += F
	return c_time + (X - C) / c_rate

def main():
	tests = int(input())
	for i in range(tests):
		print("Case #%d: %.7f" % (i+1, nextTest()))

if __name__ == '__main__':
	main()
