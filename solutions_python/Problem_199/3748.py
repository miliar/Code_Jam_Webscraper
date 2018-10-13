import sys

sys.setrecursionlimit(3000)

t = int(input())
   
def replacer(a, k):
	
	return a
	
def flip(s, m, c):
	t = s.find('-')

	a = s[t:t+m]

	if len(a) < m or c > 3000:
		return 'IMPOSSIBLE'
	else:
		a = a.replace('+','p').replace('-', 'n')
		a = a.replace('p', '-').replace('n', '+')
		b = s[:t] + a + s[t+m:]
		
		if '-' in b:
			return flip(b, m, c+1)
		else:
			return c

for i in range(1, t + 1):
	n, m = [str(s) for s in input().split(" ")]
	m = int(m)
	if '-' in n:
		numero = flip(n,m,1)

		print("Case #{}: {}".format(i,numero))
	else:
		print("Case #{}: {}".format(i, 0) )

