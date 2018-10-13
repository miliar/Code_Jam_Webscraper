#!/usr/bin/env python
import sys
import os

def main():
	n = int(sys.stdin.readline()[:-1])
	c = Pr_A()
	for i in range(1, n+1):
		c.run(i)

class Pr_A:
	def run(self, case):
		text = sys.stdin.readline()[:-1].split()
		n = int(text[0])
		del text[0]
		moves = []
		for i in range(0, n*2, 2):
			moves.append([text[i], int(text[i+1])])

		t = 0
		oo = 1
		bb = 1
		while(len(moves) > 0):
			t += 1

			od = 0
			for m in moves:
				if m[0] == "O":
					od = m[1]
					break
			bd = 0
			for m in moves:
				if m[0] == "B":
					bd = m[1]
					break
			#print '%d oo=%d od=%d bb=%d bd=%d' % (t, oo, od, bb, bd)
			#print moves
			press = False
			if od != 0:
				if oo == od:
					if moves[0][0] == "O":
						#print '%d O pressed' % (t,)
						press = True
						del moves[0]
				elif oo < od:
					oo += 1
				else:
					oo -= 1

			if bd != 0:
				if bb == bd:
					if press == False:
						if moves[0][0] == "B":
							#print '%d B pressed' % (t,)
							del moves[0]
				elif bb < bd:
					bb += 1
				else:
					bb -= 1
		output = str(t)
		print "Case #%d: %s" % (case, output)

if __name__ == '__main__':
	main()
