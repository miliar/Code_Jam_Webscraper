from math import log

def chooseStall(n, k):
	e = int(log(k, 2))
	r = n
	for i in range(e):
		k -= 2 ** i
		r -= 2 ** i
	q = n // (2 ** e)
	if k * q + (2 ** e - k) * (q - 1) > r:
		q -= 1
	if q % 2 == 0:
		return (q // 2, q // 2 - 1)
	else:
		return (q // 2, q // 2)

n = int(input())
for i in range(n):
	x, y = input().split()
	a, b = chooseStall(int(x), int(y))
	print('Case #{}: {} {}'.format(i + 1, a, b))
