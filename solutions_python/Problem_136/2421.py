#! python2
from __future__ import division
import sys


sys.stdin = open('large.in')
sys.stdout = open('large.out', 'w')

def solve(c, f, x):
	t_farm = 0
	speed = 2
	last_t = float('inf')
	while True:
		t = t_farm + x / speed
		if t > last_t:
			return last_t

		t_farm += c / speed
		speed += f
		last_t = t

n = int(raw_input())

for i in range(n):
	c, f, x = (float(x) for x in raw_input().split(' '))
	
	print "Case #{}: {}".format(i+1, solve(c, f, x))
