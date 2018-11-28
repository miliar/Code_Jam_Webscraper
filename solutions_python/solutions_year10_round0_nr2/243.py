#!/bin/python

# Observed behavior:
# After 0 snaps:  000000
# After 1 snaps:  100000
# After 2 snaps:  010000
# After 3 snaps:  110000
# After 4 snaps:  001000
# After 5 snaps:  101000
# After 6 snaps:  011000
#
# The light is on if the lowest N bits of K are all ones!

def CalcTimes(times):
	
	def GreatestCommonDivisor(x, y):
		while x and y:
			if x > y:
				x = x % y
			else:
				y = y % x
		return x + y
		
	diffs = set()
	for t1 in times:
		for t2 in times:
			diffs.add(abs(t1-t2))
	gcd = reduce(GreatestCommonDivisor, diffs)
	
	elapsed_since_previous_multiple = times[0] % gcd
	if elapsed_since_previous_multiple == 0:
		return 0
	return gcd - elapsed_since_previous_multiple
	

if __name__ == '__main__':
	for case_number in xrange(1, int(raw_input())+1):
		inputs = map(int, raw_input().split())
		times = inputs[1:]
		print "Case #%d: %s" % (case_number, CalcTimes(times))

	
	
	