def charInvert(c):
	if c == '+':
		return '-'
	elif c == '-':
		return '+'
	return ''

def invert(s):
	return ''.join([charInvert(c) for c in s])

def flip(s, k, i):
	return s[:i] + invert(s[i:i+k]) + s[i+k:]

def solve(s, k):
	length = len(s)
	flips = 0
	solSet = set(['+'*length])
	if s in solSet:
		return 0
	for i in range(length-k+1):
		newSolSet = set([flip(s1, k, j) for s1 in solSet for j in range(length-k+1)])
		if s in newSolSet:
			return i+1
		solSet = newSolSet
	return 'IMPOSSIBLE'

if __name__ == '__main__':
	T = int(input().strip())
	for i in range(T):
		data = input().strip().split(' ')
		s = data[0]
		k = int(data[1].strip())
		sol = solve(s, k)
		print('Case #{}: {}'.format(i+1, sol))