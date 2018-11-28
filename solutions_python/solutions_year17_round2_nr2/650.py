import sys
sys.setrecursionlimit(10000)
d = {'R': ['Y', 'B'], 
	 'Y': ['B', 'R'],
	 'B': ['R', 'Y']}
l = ['R', 'Y', 'B']

def f_r(i, a, c):
	if i == n-1:
		if a[0] in d[a[-1]]:
			return a
		return None
	for s in sorted(d[a[-1]], key=lambda x: c[x], reverse=True):
		if c[s] > 0:
			c[s] -= 1
			p = f_r(i+1, a+s, c)
			if p:
				return p
			c[s] += 1
	return None

def f(n, r, y, b):
	c = {'R': r, 'Y': y, 'B': b}
	l.sort(key=lambda x: c[x])
	for i in range(3):
		if c[l[i]] > 0:
			c[l[i]] -= 1
			a = f_r(0, l[i], c)
			if a:
				return a
			c[l[i]] += 1
	# print("No")
	return None

def f2(n, r, y, b):
	on, tw, thr = sorted([r, y, b], reverse=True)
	# print(on, tw + thr)
	if on == 0:
		return "IMPOSSIBLE"
	if on > tw+thr:
		return "IMPOSSIBLE"
	if thr == 0:
		if tw == 0:
			return "IMPOSSIBLE"
		if r == 0:
			return "YB" * y
		if y == 0:
			return "RB" * r
		if b == 0:
			return "RY" * r
	a = f(n, r, y, b)
	if a:
		return a
	return "IMPOSSIBLE"

t = int(input())
for it in range(1, t+1):
	n, r, o, y, g, b, v = map(int, input().split())
	out = f2(n, r, y, b)
	print("Case #%d:" % it, out)
