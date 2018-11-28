import sys
import math

if __name__ == '__main__':
	f = open(sys.argv[1])

	T = int(f.readline())

	for case in xrange(1,T+1):
		X, R, C = [int(d) for d in f.readline().split(' ')]
		if (							# These are the conditions that test if the grid can be filled
				(R * C) % X == 0 	and # Checks that X fits evenly into grid
				X < 7 				and # If X is greater than 6 Richard can enclose a space
				(min(R,C) > X/2 	or 	# Checks the shorter side
				X == 2) 			and # Edge case
				max(R,C) >= X 			# Checks the longer side 
			):
			winner = 'GABRIEL'
		else:
			winner = 'RICHARD'

		print 'Case #%d: %s' % (case, winner)