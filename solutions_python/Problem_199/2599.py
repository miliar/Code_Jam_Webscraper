
def invert(str, a, b):
	return ''.join(['-'
			if (c == '+' and a <= i < b) or (c == '-' and not(a <= i < b))
		else '+' for i, c in enumerate(str)])

T = int(input())
for t in range(T):
	str, n = input().split()
	n = int(n)
	result = 0
	for i in range(len(str)):
		if str[i] == '-' and i <= len(str) - n:
			result = result+1
			str = invert(str,i,i+n)
	if '-' in str:
		result = 'IMPOSSIBLE'
	print('Case #%s: %s' % (t+1, result))
