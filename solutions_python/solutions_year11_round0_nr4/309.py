import sys
def case(a, b):
	j=1
	ret = 0
	for d in b[:-1].split(' '):
		if int(d) != j:
			ret += 1
		j += 1
	return ret

n = sys.stdin.readline()
for i in range ((int)(n[:-1])):
	a = sys.stdin.readline()
	b = sys.stdin.readline()
	r = case(a, b)
	print 'Case #{0}: {1}.000000'.format(i+1, r)
