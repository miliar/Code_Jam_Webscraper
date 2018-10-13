import sys
from Queue import PriorityQueue

def solve(d,l,distance):
	N = len(d)
	reach = [False]*(N+1)
	reach[0]=True
	bigd = [0]*(N+1)
	bigd[0] = d[0]

	for i in range(0,N):
		for j in range(i+1,N):
			if d[i]+bigd[i]>=d[j]:
				if min(d[j]-d[i],l[j]) > bigd[j]:
					bigd[j] = min(l[j],d[j]-d[i])

	for i in range(0,N):
		if d[i]+bigd[i]>=distance:
			return "YES"

	return "NO"

def main(argv):

	if argv is None:
		print "No input file supplied"
		sys.exit(2)

	if len(argv) < 3:
		print "No output file supplied"
		sys.exit(2)

	_in = open(argv[1], 'r')
	_out = open(argv[2], 'w')
	_tst, _line = int(_in.readline()), None
	
	for i in range(0,_tst):
		_line = _in.readline().strip('\n')
		###################
		N = int(_line)
		d = [0]*N
		l = [0]*N
		for j in range(0,N):
			_line = _in.readline().strip('\n')
			t = _line.split(' ')
			d[j], l[j] = int(t[0]), int(t[1])
		_line = _in.readline().strip('\n')
		dist = int(_line)
		###################
		_sol = solve(d,l,dist)
		_output = "Case #%d: %s\n" % (i+1, _sol)
		print _output
		if i == _tst-1:
			_output.strip('\n')
		_out.write(_output)
	_out.flush()
	_out.close()

main(argv=sys.argv)

