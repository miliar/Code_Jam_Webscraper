import psyco
psyco.full()


def solve(N):
	impo, minWin = findImportant(N)
	if impo == -1:
		N = list(N)
		N.sort()
		N.insert(1, '0')
		while N[0] == '0':
			N.pop(0)
			N.insert(nonZero(N)+1, '0')
		N = ''.join(N)
		return N
	notouch = N[:impo]
	fix = list(N[impo:])
	fix.remove(minWin)
	fix.sort()
	
	return  notouch + minWin + ''.join(fix)

def nonZero(N):
	i = 0
	while N[i] == '0':
		i += 1
	return i

def findImportant(N):
	i = len(N) - 1
	passed = set()
	minWin = 0
	while i != -1:
		passed.add(N[i])
		for j in list(passed):
			if N[i-1] < j:
				tmp = list(passed)
				tmp.sort()
				for k in tmp:
					if k > N[i-1]:
						return i-1, k
		i += -1
	return i, 0
	

data = open('b.txt', 'r').read().split('\n')

(T,) = map(int, data.pop(0).split(' '))

for i in xrange(T):
	
	N = data.pop(0).strip()
	print 'Case #' + str(i+1) + ': ' + solve(N)
