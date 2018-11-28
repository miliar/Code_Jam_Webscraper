from cjlib.input import *
from cjlib.runner import TaskRunner, DummyRunner, MPQRunner
import logging, copy

logging.basicConfig(level=logging.INFO)

def notFinished(case, inp):
	for y, l in enumerate(case):
		for x, v in enumerate(l):
			if v != inp[y][x]:
				return True
	return False

def notFinishedList(case, inp):
	case = copy.deepcopy(case)
	for y, l in enumerate(case):
		for x, v in enumerate(l):
			if v == inp[y][x]:
				case[y][x] = 0
	return case

def isOkayX(inp, sol, line, mx):
	# cut down!
	cutDoAnything=False
	for ind,l in enumerate(inp):
		if l[line] < mx or sol[ind][line] > mx:
			return False
		if l[line] > mx:
			cutDoAnything = True
	logging.debug("Will cut: %s Y Line %s to %s", cutDoAnything, line, mx)
	return cutDoAnything
def cutX(inp, line, mx):
	# cut down
	for ind,l in enumerate(inp):
		inp[ind][line] = mx
	return inp

def isOkayY(inp, sol, line, mx):
	cutDoAnything=False
	for pos,l in enumerate(inp[line]):
		if l < mx or sol[line][pos] > mx:
			return False
		if l > mx:
			cutDoAnything = True
	return cutDoAnything
def cutY(inp, line, mx):
	# cut right
	for ind,l in enumerate(inp[line]):
		inp[line][ind] = mx
	return inp
def myMax(arr):
	try:
		return max(arr)
	except ValueError:
		return 0

def process(case):
	out=[]
	for y in range(len(case)):
		l = []
		for x in range(len(case[0])):
			l.append(100)
		out.append(l)
	while notFinished(case, out):
		mx = myMax([myMax(x) for x in notFinishedList(case, out)])
		cutted = False
		# find edge to get in
		for x, notused in enumerate(out[0]):
			if isOkayX(out, case, x, mx):
				logging.debug("Cut Y%d to %d", x, mx)
				out = cutX(out, x, mx)
				#print case, "\n", out
				cutted=True
				break
		if cutted:
			continue
		for y, notused in enumerate(out):
			if isOkayY(out, case, y, mx):
				cutted=True
				logging.debug("Cut X%d to %d", y, mx)
				out = cutY(out, y, mx)
				#print case, "\n", out
				break
		if not cutted:
			return "NO"
	return "YES"

get("""3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1""")

r = TaskRunner(process, MPQRunner)

while neof():
	size = [int(x) for x in line().split(" ")]
	grid = []
	for x in xrange(size[0]):
		grid.append([int(x) for x in line().split(" ")])
	r.add(grid)

r.run(True)