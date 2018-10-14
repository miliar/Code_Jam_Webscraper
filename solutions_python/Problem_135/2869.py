from __future__ import division
from cjlib.input import *
from cjlib.runner import TaskRunner, MPQRunner, DummyRunner
from itertools import permutations

get("""3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16""")

def process(data):
	firstRow = int(data[0])
	firstArr = [[int(y) for y in x.split(" ")] for x in data[1]]
	lastRow = int(data[2])
	lastArr = [[int(y) for y in x.split(" ")] for x in data[3]]
	
	pickFirst = firstArr[firstRow-1]
	pickLast = lastArr[lastRow-1]

	intersect = [x for x in pickFirst if x in pickLast]
	if len(intersect) == 1:
		return intersect[0]
	elif len(intersect) > 1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"

r = TaskRunner(process, DummyRunner)

while neof():
	r.add([line(),  lines(4), line(), lines(4)])

r.run(True)