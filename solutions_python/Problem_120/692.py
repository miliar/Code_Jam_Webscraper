from cjlib.input import *
from cjlib.runner import TaskRunner, DummyRunner, MPQRunner
import logging

logging.basicConfig(level=logging.INFO)

def process(case):
	# all units in pi cm^2
	paintLeft = case[1]
	canDraw = 0
	currentSize = case[0] + 1
	while paintLeft > 0:
		paintShouldBeLeft = paintLeft - ((currentSize ** 2) - ((currentSize-1)**2))
		if paintShouldBeLeft >= 0:
			paintLeft = paintShouldBeLeft
			canDraw += 1
		else:
			break
		currentSize += 2
	return canDraw

get("""5
1 9
1 10
3 40
1 1000000000000000000
10000000000000000 1000000000000000000""")

r = TaskRunner(process, MPQRunner)

while neof():
	l = [int(x) for x in line().split(" ")]
	r.add(l)

r.run(True)