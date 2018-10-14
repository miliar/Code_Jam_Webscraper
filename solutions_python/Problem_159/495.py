import sys

def method1(m):
	total = 0
	plate = m[0]
	for i in range(1, len(m)):
		current = m[i]
		if current < plate:
			total += (plate - current)
		plate = current
	return total

def method2(m):
	delta = 0
	for i in range(1, len(m)):
		diff = m[i-1] - m[i]
		if diff > delta:
			delta = diff
	total = 0
	plate = m[0]
	for i in range(1, len(m)):
		current = m[i]
		if plate < delta:
			total += plate
		else:
			total += delta
		plate = current
	return total

def answer(N, m):
	if N != len(m):
		print 'Error'
	else:
		return [method1(m), method2(m)]

if __name__ == '__main__':
	f = sys.stdin
	fn = sys.argv[1]
	f = open(fn)
	if len(sys.argv) == 3:
		output = open(sys.argv[2], 'w')
	t = int(f.readline())
	for _t in xrange(t):
		N = int(f.readline().strip())
		m = map(int, f.readline().split())
		ans = answer(N, m)
		if len(sys.argv) == 3:
			output.write('Case #%d: %d %d' % (_t+1, ans[0], ans[1]) + '\n')
		print 'Case #%d: %d %d' % (_t+1, ans[0], ans[1])
