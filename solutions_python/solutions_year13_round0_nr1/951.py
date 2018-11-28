from __future__ import print_function
import sys

sys.stdin = open("A.in")
sys.stdout = open("A.out", "w")

N = int(raw_input())

for test in range(N):
	field = [ raw_input() for i in range(4) ]
	
	#print(field)
	
	def row(field, x, letter):
		return all( i in (letter,'T') for i in field[x] )
	def col(field, x, letter):
		return all( i[x] in (letter,'T') for i in field )
	def di(field, letter):
		return all( field[i][i] in (letter,'T') for i in range(4) ) or \
			all( field[3 - i][i] in (letter,'T') for i in range(4) )
	
	check = 'O', 'X'
	
	won = dict( [(i, False) for i in check] )
	
	for c in check:
		won[c] = any( row(field, i, c) for i in range(4) )
		won[c] = won[c] or any( col(field, i, c) for i in range(4) )
		won[c] = won[c] or di(field, c)
	
	print("Case #%d: " % (test + 1), end = "")
	
	#print(won)
	
	if won['O'] and won['X']:
		print("Draw")
	elif won['O']:
		print("O won")
	elif won['X']:
		print("X won")
	else:
		# Either draw or not completed
		notcompl = any( '.' in i for i in field )
		
		if notcompl:
			print("Game has not completed")
		else:
			print("Draw")

	try:
		raw_input() # skip the empty line
	except:
		pass