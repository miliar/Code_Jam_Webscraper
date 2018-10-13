from cjlib.input import *
from cjlib.runner import TaskRunner, DummyRunner
import logging

logging.basicConfig(level=logging.DEBUG)

def flipWorld(data):
	o = [["","","",""],["","","",""],["","","",""],["","","",""]]
	#print o
	for x,d in enumerate(data):
		for y,d2 in enumerate(d):
			o[y][x] = d2
	#print o, y, x, d2
	return o
def checkDiagonal(data, xy):
	# xy start
	if xy == 0:
		x = data[xy][xy] + data[xy+1][xy+1] + data[xy+2][xy+2] + data[xy+3][xy+3]
	elif xy == 3:
		x = data[0][xy] + data[1][xy-1] + data[2][xy-2] + data[3][xy-3]
		#print x, data
	if ("XXX" in x and "T" in x) or x == "XXXX":
		return "X won"
	elif ("OOO" in x and "T" in x) or x == "OOOO":
		return "O won"
	else:
		return None

def process(case):
	out = ""
	hasDot = False
	for x in case:
		if "." in x:
			hasDot = True
		if ("XXX" in x and "T" in x) or x == "XXXX":
			return "X won"
		elif ("OOO" in x and "T" in x) or x == "OOOO":
			return "O won"
	f = flipWorld(case)
	for x in f:
		x = "".join(x)
		if ("XXX" in x and "T" in x) or x == "XXXX":
			return "X won"
		elif ("OOO" in x and "T" in x) or x == "OOOO":
			return "O won"
	dia = [checkDiagonal(f, 0), checkDiagonal(f, 3)]
	for x in dia:
		if x != None:
			return x
	if not hasDot:
		return "Draw"
	else:
		return "Game has not completed"

get("""6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O""")

r = TaskRunner(process, DummyRunner)

while neof():
	data = lines(4)
	if neof():
		line()
	r.add(data)

r.run(True)