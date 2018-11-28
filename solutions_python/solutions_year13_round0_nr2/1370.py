


def solve(n, m, matrix):
	rowsmaxs = [max(l) for l in matrix]
	columnsmaxs = [max(l) for l in zip(*matrix)]
	for i in xrange(n):
		for j in xrange(m):
			if( matrix[i][j] < rowsmaxs[i] and matrix[i][j] < columnsmaxs[j] ):
				return "NO"
				
	return "YES"


f = open('inputs', 'r')
o = open('outputs', 'w')

T = int(f.readline().strip())

for t in xrange(T):
	n , m = map(int, f.readline().strip().split())
	case = []
	for i in range(n):
		line = map(int,f.readline().strip().split())
		case.append(line)
	s = "Case #%d: %s\n" % (t+1, solve(n,m,case))
	o.write(s)
	print(s)
f.close()
o.close()	
