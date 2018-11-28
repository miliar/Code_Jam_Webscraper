def flip(s,p,n):
	return s[:p] + ''.join(map(fc, list(s[p:p+n])))+s[p+n:]

def fc(c):
	if c == '+':
		return '-'
	else:
		return '+'


def solve(s,n):
	m = len(s)
	moves = 0
	for i in range(n,m+1):
		if s[i-n] == '+':
			continue
		s=flip(s,i-n,n)
		moves +=1
	for i in range(m):
		if s[i] == '-':
			return 'IMPOSSIBLE'
	return str(moves)

T = int(input())
for case in range(1,T+1):
	s,n = input().split()
	print("Case #{}: {}".format(case, solve(s,int(n))))
