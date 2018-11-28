#!/bin/python3

def solve(c, f, x):
	#return time if just wait
	def wait(rate):
		return x/rate
	#return time to wait until can buy
	def buy(rate):
		return c/rate
	def buy_wait(rate):
		return buy(rate) + wait(rate + f)
	r = 2
	total_time = 0

	while buy_wait(r) < wait(r):
		total_time += buy(r)
		r += f

	return total_time + wait(r)

num_cases = int(input())
for casenum in range(1, num_cases+1):
	C, F, X = [float(z) for z in input().split()]	
	print ("Case #{0}: {1}".format(casenum, solve(C, F, X)))