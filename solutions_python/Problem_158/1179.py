#!/usr/bin/python

f = open('D-small-attempt0.in', 'r')
w = open('D-small-attempt0.out', 'w')

n_cases = f.readline()
#print "cases:" + n_cases

cases = f.read().splitlines()
n_case = 1
n = 0
winner = ""
for case in cases:
		game = case.split(" ")
		x = int(game[0])
		r = int(game[1])
		c = int(game[2])

		if x == 1:
			winner = "GABRIEL"
		elif x == 2:
			if (r*c) % 2 == 1:
				winner = "RICHARD"
			else:
				winner = "GABRIEL"
		elif x == 3:
			if (r*c) % 3 != 0 or r == 1 or c == 1:
				winner = "RICHARD"
			else:
				winner = "GABRIEL"
		elif x == 4:
			if (r*c) % 4 != 0 or r*c == 4 or r*c == 8 or r == 1 or c == 1:
				winner = "RICHARD"
			else:
				winner = "GABRIEL"
 
		#print "--"
		print "Case #" +  str(n_case) + ": " + winner
		#print "--"
		if n_case < int(n_cases):
			w.write("Case #" +  str(n_case) + ": " + winner + "\n")
		else:
			w.write("Case #" +  str(n_case) + ": " + winner)

		n = 0
		n_case += 1

f.closed
w.closed