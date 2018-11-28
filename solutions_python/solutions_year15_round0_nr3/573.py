def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())

mult = {}
mult['1'] = dict(zip(['1', 'i', 'j', 'k'], [(1, '1'), (1, 'i'), (1, 'j'), (1, 'k')]))
mult['i'] = dict(zip(['1', 'i', 'j', 'k'], [(1, 'i'), (-1, '1'), (1, 'k'), (-1, 'j')]))
mult['j'] = dict(zip(['1', 'i', 'j', 'k'], [(1, 'j'), (-1, 'k'), (-1, '1'), (1, 'i')]))
mult['k'] = dict(zip(['1', 'i', 'j', 'k'], [(1, 'k'), (1, 'j'), (-1, 'i'), (-1, '1')]))


_T = readint()

for _t in range(_T):
	print('Case #%i:'%(_t+1)),

	L, X = readarray(int)

	s = list(raw_input()) * X
	
	if L*X < 3:
		print "NO"
		continue


	sign = 1
	while len(s) > 3 and s[-1] != 'k':
		c = s.pop()
		sig, s[-1] = mult[s[-1]][c]
		sign *= sig

	if s[-1] != 'k':
		print "NO"
		continue

	s.pop()


	while len(s) > 2 and s[-1] != 'j':
		c  = s.pop()
		sig, s[-1] = mult[s[-1]][c]
		sign *= sig

	if s[-1] != 'j':
		print "NO"
		continue

	s.pop()

	while len(s) > 1 and s[-1] != 'i':
		c  = s.pop()
		sig, s[-1] = mult[s[-1]][c]
		sign *= sig

	if s[-1] != 'i':
		print "NO"
		continue

	s.pop()

	while len(s)>1:
		c = s.pop()
		sig, s[-1] = mult[s[-1]][c]
		sign *= sig

	if (not s or s[0] == '1') and sign == 1:
		print "YES"
	else:
		print "NO"

