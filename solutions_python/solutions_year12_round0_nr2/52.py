# Tested and running on: 
# Python 2.7.2 (default, Jan 20 2012, 15:37:52) 
# [GCC 4.2.1 Compatible Apple Clang 3.0 (tags/Apple/clang-211.12)] on darwin

# (C) 2012 Dennis Bliefernicht

def process():
	inline = map(lambda x: int(x), pop().split(" "))
	ngoog = inline[0]
	surpr = inline[1]
	least = inline[2]
	scores = inline[3:]
	
	# analysis shows that there are 3 cases with score mod 3 is 0, 1, 2
	# for each score check if it makes a difference to make this one surprising
	numanyway = 0 # number of scores above the limit anyway
	numsuprising = 0 # number of scores only above the limit if surprising
	for s in scores:
		m = s % 3
		
		if m == 0:
			nosup = s / 3
			sup = (s / 3) + 1
		elif m == 1:
			nosup = (s / 3) + 1
			sup = (s / 3) + 1
		else:
			nosup = (s / 3) + 1
			sup = (s / 3) + 2
			
		if s == 0:
			nosup = 0
			sup = 0
			
		if (nosup >= least) and (sup >= least):
			numanyway += 1
		elif (nosup < least) and (sup >= least):
			numsuprising += 1
	
	# now the maximum is the number of anyway plus the number of surprising capped by the number of observed surprising
	if numsuprising < surpr:
		result = numanyway + numsuprising
	else:
		result = numanyway + surpr
		
	out(result)

# ------------------------------------
# GCJ2012 framework stuff
# ------------------------------------
import sys
import os

case_number = 1
lines = []

def out(*vals):
	global case_number
	print "Case #%d:" % case_number,
	for v in vals:
		print str(v),
	print
	case_number += 1
		
def output(fmt, *vals):
	global case_number
	print ("Case #%d: " + fmt) % ((case_number,) + vals)
	case_number += 1

def pop():
	global lines
	e = lines[0]
	lines = lines[1:]
	return e
	
def popint():
	return int(pop())
	
def popflt():
	return float(pop())
	
def main():
	global lines
	case_count = int(pop())
	for x in range(case_count):
		process()
	if len(lines) != 0:
		print "ERROR: %d lines remaining" % (len(lines))

if __name__ == "__main__":
	f = open(sys.argv[1])
	lines = map(lambda x: x[:-1], f.readlines())
	f.close()
	main()