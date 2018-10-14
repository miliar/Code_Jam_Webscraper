# coding: utf8
# rozwiązanie ?
import sys


def min_switches(engines, queries):
	used_max= len(engines)
	used	= set()

	switches	= 0
	for q in queries:
		used.add(q)
		if len(used) == used_max:
			switches += 1
			used.clear()
			used.add(q)
	return switches


if len(sys.argv) > 1:
	f_name = sys.argv[1]
else:
	f_name = "su.in"

f = open(f_name)
N = int(f.readline())

for i in xrange(N):
	S	= int(f.readline())
	engines	= []
	for j in xrange(S):
		engines.append(f.readline())

	Q	= int(f.readline())
	queries	= []
	for j in xrange(Q):
		queries.append(f.readline())
	switches = min_switches(engines, queries)
	print "Case #%d: %d" % (i+1, switches)


