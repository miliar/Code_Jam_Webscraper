from __future__ import print_function
import sys

sys.stdin = open("B.in")
sys.stdout = open("B.out", "w")

T = int(raw_input())

for test in range(T):
	r, c = map( int , raw_input().split() )
	field = [ map( int , raw_input().split() ) for i in range(r) ]
	
	assert len(field[0]) == c
	
	myall = [ (field[x][y], (x,y)) for x in range(r) for y in range(c) ]
	
	myall.sort(reverse = True)
	
	def cutrow(x, max):
		return all( (field[x][i] <= max for i in range(c)) )
	def cutcol(x, max):
		return all( (field[i][x] <= max for i in range(r)) )
	
	print("Case #%d: " % (test + 1), end = "")
	
	for value, (x,y) in myall:
		if not cutrow(x, value) and not cutcol(y, value):
			print("NO")
			break
	else:
		print("YES")
	
	