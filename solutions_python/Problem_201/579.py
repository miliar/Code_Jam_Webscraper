import sys
sys.stdin = open('C.txt', 'r')
sys.stdout = open('C.out', 'w')

def solve(n, k):
	c = [0, 0]
	cn = [0, 0]
	c[n%2], cn[n%2] = 1, n
	c[not(n%2)], cn[not(n%2)] = 0, n + 1 - 2 * (n%2)
	total = 0
	while True:
		bigger = 1 if cn[1] > cn[0] else 0
		total += c[bigger]
		if total >= k: return cn[bigger]
		total += c[not bigger]
		if total >= k: return cn[not bigger]
		cn2 = [cn[0] // 2, cn[0] // 2]
		if cn2[0] % 2 == 1: cn2[0] -= 1
		else: cn2[1] -= 1
		c2 = [c[0], c[0]]
		c2[cn2.index(cn[1] // 2)] += 2 * c[1]
		c, cn = c2, cn2

def process(ans):
	d, m = divmod(ans - 1, 2)
	return str(d + m) + ' ' + str(d)

T = input()
lines = [list(map(int, raw_input().split())) for _ in range(T)]
print '\n'.join('Case #{}: {}'.format(i + 1, process(solve(n, k))) for i, (n, k) in enumerate(lines))
