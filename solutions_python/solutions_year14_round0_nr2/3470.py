#!/bin/python

# we need to check if buying + target_after_buying < target_after_buying

def do_magic(start, end, f, rate, c, prev = 0):
	while 1:
		diff = end - start
		without_farm = round(float(diff) / float(rate), 7)
		with_farm = round(float(c) / float(rate) + float(diff) / float(rate + f), 7)
		#print "Without Farm =", without_farm
		#print "With Farm =", with_farm 
		if with_farm > without_farm:
			return prev + without_farm

		prev = prev + round(float(float(c) / float(rate)), 7)
		rate += f

t = input()
i = 1
while i <= t:
	inp = raw_input().split()
	inp = [float(a) for a in inp]
	c, f, x = inp

	print "Case #%d: %.7f" % (i, round(do_magic(0, x, f, 2, c), 7))
	i += 1