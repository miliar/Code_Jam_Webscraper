#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
	sys.ext("Usage: " + sys.argv[0] + "<input>")

f = open(sys.argv[1], 'r')

def solve( c, f, x ):
	cps = 2
	num_farms = 0

	# x = (cps * t) + (f * t * num_farms) - (c * num_farms)

	sum_t = 0;
	t = 0 # don't buy a new farm
	T = x / cps # time to complete after buying a farm
	nt = c / cps # time to complete after buying that new farm
	nT = x / (cps + f)
	while sum_t + t + T > sum_t + t + nt + nT :
		num_farms += 1
		sum_t += t
		t = nt
		T = nT
		nt = c / (cps + f * num_farms) # time to buy a new farm
		nT = x / (cps + f * (num_farms + 1)) # time to complete after buying that new farm
	return sum_t + t + T
		

games = int(f.readline())
game = 0
while game < games:
	line = list(map(float,f.readline().split()))
	time = solve( line[0], line[1], line[2] )
	game += 1
	print("Case #" + str(game) + ": " + str(time))

