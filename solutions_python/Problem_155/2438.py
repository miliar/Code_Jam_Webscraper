import sys

def solve(s,arr):
	total = 0
	max = 0
	#print arr
	for i in xrange(s+1):
		if i > total:
			t = i-total
			if t > max: max = t
		total += arr[i]

	return max
T = int(sys.stdin.readline())
case = 1
for _ in xrange(T):
	s,string = sys.stdin.readline().strip().split(' ')
	s = int(s)
	arr = map(int,list(string))
	print 'Case #%d: %d' %(case,solve(s,arr))
	case += 1