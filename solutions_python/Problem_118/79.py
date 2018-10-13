import bisect

good = []

def rec(s, x, sum):
	if sum < 0:
		return
	if x == len(s) / 2:
		good.append(''.join(s))
	else:
		rec(s, x + 1, sum)
		if s[x] == '0':
			s[x] = s[- x - 1] = '1'
			rec(s, x + 1, sum - 2)
			s[x] = s[- x - 1] = '0'

def precalc():
	good.append('1')
	good.append('2')
	good.append('3')
	for len in range(2, 51):
		s = ['0']*len
		sum = 9
		for bnd in ['1', '2']:
			s[0] = 	s[-1] = bnd
			sum -= 2 * (ord(bnd) - ord('0'))**2
			for center in ['0', '1', '2']:
				sum -= (ord(center) - ord('0'))**2
				if len % 2 == 1:
					s[len / 2] = center
				rec(s, 1, sum)
				if len % 2 == 0:
					break
				sum += (ord(center) - ord('0'))**2
			sum += 2 * (ord(bnd) - ord('0'))**2

precalc()
#open('tmp.txt', 'w').write('\n'.join(good))
#print len(good)
#exit(0)
data = map(lambda x: x**2, sorted(map(lambda x: int(x), good)))
inp = open('C-large-2.in')
out = open('C-large-2.out', 'w')

T = int(inp.readline())
for test in range(T):
	line = inp.readline()
	l = int(line.strip().split(' ')[0])
	r = int(line.strip().split(' ')[1])
	r = bisect.bisect_right(data, r)
	l = bisect.bisect_left(data, l) - 1
	print >> out, 'Case #%d: %d' % (test + 1, r - l - 1)

inp.close()
out.close()
