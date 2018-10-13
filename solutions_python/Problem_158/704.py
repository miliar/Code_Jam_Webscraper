
# We do the small input by hand and let Python handle writing up
# our answers.

T = int(raw_input().strip())
for t in xrange(T):
	(X, R, C) = map(int, raw_input().strip().split(" "))
	if X == 1:
		g_wins = True  # true if Gabriel can win
	elif X == 2:
		if 0 != R % 2 and 0 != C % 2:
			g_wins = False
		else:
			g_wins = True
	elif X == 3:
		if 0 != R % 3 and 0 != C % 3:
			g_wins = False
		elif 1 == R or 1 == C:
			g_wins = False
		else:
			g_wins = True
	elif X == 4:
		if 0 != (R * C) % 4:
			g_wins = False
		elif R < 4 and C < 4:
			g_wins = False
		elif R == 4:
			if C == 3 or C == 4:
				g_wins = True
			else:
				g_wins = False
		elif C == 4:
			if R == 3:
				g_wins = True
			elif R == 2 or R == 1:
				g_wins = False
	if g_wins:
		winner = "GABRIEL"
	else:
		winner = "RICHARD"
	print "Case #%d: %s" % (t+1, winner)
