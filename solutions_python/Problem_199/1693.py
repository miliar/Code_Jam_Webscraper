def flip(s, k, start):
	s = list(s)
	for i in range(k):
		s[start+i] = '+' if s[start+i]=='-' else '-'
	s = ''.join(s)
	return s

def solve(s, k, n):

	#impossible?


	while s.count('-') != 0:
		ind = s.index('-')
		if ind + k > len(s):
			return 'IMPOSSIBLE'
		s = flip(s, k, ind)
		n += 1
	return n

T = int(input())

s = []
k = []

for i in range(T):
	x = input().split()
	s.append(x[0])
	k.append(int(x[1]))

cnt = 1
for i in range(T):
	print('Case #%d: '%cnt,end='')
	cnt += 1
	print(solve(s[i], k[i], 0))