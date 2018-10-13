import sys

#from alg import *; solve([('O', 2), ('B', 1), ('B', 2), ('O', 4)])
#sys.exit(0)

f = open("input", "r")

lines = f.readlines()
f.close()
count = int(lines[0])

for i in xrange(count):
	question = lines[i + 1]

	numPresses = int(question[0:question.find(' ')])
	presses = question[question.find(' ')+1:]
	rpr = presses

	q = []
	for p in xrange(numPresses):
		bot = rpr[0]
		rpr = rpr[2:]
		button = int(rpr[0:rpr.find(' ')])
		rpr = rpr[rpr.find(' ')+1:]

		q += [ (bot, button) ]

	from alg import solve
	#print q
	n = solve(q)
	print "Case #%s: %s" % (i+1, n)
