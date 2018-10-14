import sys
inp = sys.stdin
T = int(inp.readline())

def read_ints():
	return [int(x) for x in raw_input().strip().split()]

for t in range(1, T+1):
	print 'Case #'+str(t)+':',
	A1 = int(inp.readline())
	rows1 = [read_ints(),read_ints(),read_ints(),read_ints()]
	A2 = int(inp.readline())
	rows2 = [read_ints(),read_ints(),read_ints(),read_ints()]
	r1 = rows1[A1-1]
	r2 = rows2[A2-1]
	k = res = 0
	for r in r1:
		if r in r2:	 k, res = k+1, r
	if k==0: print 'Volunteer cheated!'
	if k==1: print res
	if k >1: print 'Bad magician!'
