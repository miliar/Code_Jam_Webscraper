import sys

#from alg import *; solve([('O', 2), ('B', 1), ('B', 2), ('O', 4)])
#sys.exit(0)

f = open(sys.argv[1], "r")

lines = f.readlines()
f.close()
count = int(lines[0])

for i in xrange(count):
	qn = lines[2*i + 1].replace("\n", "")
	qn2 = lines[2*i + 2].replace("\n", "")

	q = map(int, qn2.split(" "))

	from alg import solve
	n = solve(q)
	if n == None:
		n = "NO"
	print "Case #%s: %s" % (i+1, n)
