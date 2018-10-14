import sys
import re
from Numeric import *

# ---------------------------------------------------------------------------------------------------------------

sys.setcheckinterval(10000)
PI = arccos(-1)
PI_2 = arccos(-1) / 2

# ---------------------------------------------------------------------------------------------------------------
# Global variables
#src_table = array(zeros(256), Int)

# ---------------------------------------------------------------------------------------------------------------

def toMins(hm):
	h = int(hm[0:2])
	m = int(hm[3:5])
	return h * 60 + m

def solve(caseNum):
	T = int(sys.stdin.readline().strip())
	NA, NB = map(int, sys.stdin.readline().strip().split(" "))

	trips = []	
	for i in range(0, NA):
		dep, arr = map(toMins, sys.stdin.readline().strip().split(" "))
		trips.append((dep, arr, 0))
	for i in range(0, NB):
		dep, arr = map(toMins, sys.stdin.readline().strip().split(" "))
		trips.append((dep, arr, 1))

	trips.sort()

	t = []
	t.append(0)
	t.append(0)
	tr = []
	tr.append([])
	tr.append([])

	for v in trips:
		tr[v[2]].sort(lambda x, y: y - x)
		if len(tr[v[2]]) == 0 or tr[v[2]][len(tr[v[2]])-1] > v[0]:
			t[v[2]] += 1
		else:
			tr[v[2]].pop()
		other = 1 - v[2]
		tr[other].append(v[1] + T)


	sys.stdout.write("Case #%d: %d %d" % (caseNum, t[0], t[1]))

# ---------------------------------------------------------------------------------------------------------------

casesCount = int(re.findall(r'[\d]+', sys.stdin.readline())[0])
first = True
for case in range(1, casesCount + 1):
	if(first):
		first = False
	else:
		print ""
	solve(case)
