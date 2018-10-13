import sys

cases = int(raw_input())

for current_case in range(1, cases+1):
	P = [int(k) for k in raw_input().split()]
	X, R, C = P[0], P[1], P[2]
	R,C = min(R,C), max(R,C)
	win = False
	if X > C or (X+1)/2 > R: # place X in a row
		win = False
	elif X >= 7: # second on problem page: not able to fill the hole
		win = False
	elif (R*C) % X != 0: # must fill the whole board with no spillover
		win = False
	elif X == 1:
		win = True
	elif X == 2:
		win = True
	elif X == 3:
		win = True
	elif X == 4:
		win = False if R==2 and C==4 else True
	
	print "Case #%d: %s" % (current_case, "GABRIEL" if win else "RICHARD")