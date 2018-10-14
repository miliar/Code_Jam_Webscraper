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

def CalcState(N, K):
	mask = (1 << N) - 1
	if (K & mask) == mask:
		return "ON"
	else:
		return "OFF"

if __name__ == '__main__':
	for case_number in xrange(1, int(raw_input())+1):
		N, K = map(int, raw_input().split())
		state = CalcState(N, K)
		print "Case #%d: %s" % (case_number, state)

	
	
	