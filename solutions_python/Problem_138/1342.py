#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
	sys.exit("Usage: " + sys.argv[0] + " <input>")

f = open(sys.argv[1], 'r')

def minmax(val, arr):
	a = []
	for i in arr:
		if i > val:
			a.append(i)

	if len(a) > 0:
		return min(a)

	return -1

def deceitful_war(player1, player2):
	naomi = player1.copy()
	ken = player2.copy()
	n = k = 0

	while len(naomi) > 0:
		chosen_ken = min(ken)
		mm = minmax(chosen_ken, naomi)
		if mm > 0:
			chosen_naomi = mm
		else:
			chosen_naomi = min(naomi)

		if chosen_naomi > chosen_ken:
			n += 1
		else:
			k += 1

		naomi.remove(chosen_naomi)
		ken.remove(chosen_ken)
				
	return n

def war(player1, player2):
	naomi = player1.copy()
	ken = player2.copy()
	n = k = 0

	for i in naomi:
		if max(ken) > i:
			ken.remove(minmax(i,ken))
			k += 1
		else:
			n += 1
				
	return n

def solve(player1, player2):
	return str(deceitful_war(player1, player2)) + " " + str(war(player1, player2))

games = int(f.readline())
game = 0
while game < games:

	rocks = int(f.readline())
	naomi = list(map(float,f.readline().split()))
	ken = list(map(float,f.readline().split()))
	
	result = solve(naomi, ken)

	game +=1
	print("Case #" + str(game) + ": " + result)
