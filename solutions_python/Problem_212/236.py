import sys
sys.stdin = open('A-small-attempt0.in', 'r')
sys.stdout = open('A-small-attempt0.out', 'w')

for tc in range(int(input())):
	n, p = map(int, input().split())
	a = list(map(lambda x: int(x)%p, input().split()))
	b = [a.count(i) for i in range(p)]

	ret = 0
	if p==2:
		ret = b[0] + (b[1]+1)//2
	elif p==3:
		k = max(b[1], b[2]) - min(b[1], b[2])
		ret = b[0] + min(b[1], b[2]) + (k+2)//3
	else:
		k = max(b[1], b[3]) - min(b[1], b[3])
		ret = b[0] + (b[2]+1)//2 + min(b[1], b[3]) +(k+3)//4

	print('Case #%d: %d' % (tc+1, ret))
