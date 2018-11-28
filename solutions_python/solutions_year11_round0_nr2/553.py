import sys

#from alg import *; solve([('O', 2), ('B', 1), ('B', 2), ('O', 4)])
#sys.exit(0)

f = open(sys.argv[1], "r")

lines = f.readlines()
f.close()
count = int(lines[0])

for i in xrange(count):
	q = lines[i + 1].replace("\n", "")

	numCombo = int(q[0:q.find(' ')])
	q = q[q.find(' ')+1:]

	combos = []
	for c in xrange(numCombo):
		combo = q[0:q.find(' ')]
		q = q[q.find(' ')+1:]

		combos += [ combo ]

	numOpposed = int(q[0:q.find(' ')])
	q = q[q.find(' ')+1:]

	opposed = []
	for c in xrange(numOpposed):
		op = q[0:q.find(' ')]
		q = q[q.find(' ')+1:]

		opposed += [ op ]
	
	q = q[q.find(' ')+1:]

	from alg import solve
	n = solve(combos, opposed, q)
	print "Case #%s: %s" % (i+1, n)
