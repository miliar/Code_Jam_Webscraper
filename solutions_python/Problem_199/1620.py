import sys

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A-large.out', 'w')

n = int(input())

for t in range(n):
	a, k = input().split()
	a = list(a)
	k = int(k)
	r = 0

	for i in range(len(a)-k+1):
		if a[i] == '-':
			for j in range(i, i+k):
				if a[j] == '-': a[j] = '+'
				else: a[j] = '-'
			r += 1

	print('Case #%d: ' % (t+1), end = '')
	fl = 0
	for i in range(len(a)):
		if a[i] == '-':
			fl = 1
			print('IMPOSSIBLE')
			break

	if not fl: print(r)