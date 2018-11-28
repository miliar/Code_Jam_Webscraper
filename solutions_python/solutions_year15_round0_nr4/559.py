def gabeWins(t):
	print "Case #"+str(t+1)+": GABRIEL"

def richardWins(t):
	print "Case #"+str(t+1)+": RICHARD"

for t in range(input()):
	X, R, C = map(int, raw_input().split())
	if max(X,R,C) <= 4:
		if X == 1:
				gabeWins(t)
		elif X == 2:
			if R*C % 2 == 0:
				gabeWins(t)
			else:
				richardWins(t)
		elif X == 3:
			if R*C in [6,9,12]:
				gabeWins(t)
			else:
				richardWins(t)
		elif X == 4:
			if R*C in [12, 16]:
				gabeWins(t)
			else:
				richardWins(t)
	else:
		if X >= 7:
			richardWins(t)
		elif X == 1:
			gabeWins(t)
		elif X == 2:
			if R*C % 2 == 0:
				gabeWins(t)
			else:
				richardWins(t)
		elif X == 3:
			if R*C % 3 != 0 or min(R,C) == 1:
				richardWins(t)
			else:
				gabeWins(t)
		elif X == 4:
			if R*C % 4 != 0 or R*C < X:
				richardWins(t)
			else:
				gabeWins(t)
		elif X == 5:
			if R*C % 5 != 0 or R*C < X:
				richardWins(t)
			else:
				gabeWins(t)
		elif X == 6:
			if R*C % 6 != 0 or R*C < X:
				richardWins(t)
			else:
				gabeWins(t)