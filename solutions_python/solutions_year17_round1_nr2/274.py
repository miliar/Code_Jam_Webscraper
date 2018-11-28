from math import floor
def f2(n, p, ign, a):
	ls = []
	c = 0
	lc = []
	for i in range(n):
		ic = 0
		s = {}
		for j in range(p):
			d = round(a[i][j] / ign[i])
			# print('r', d, ign[i] * d * 0.9)
			d0 = d
			while ign[i] * d * 0.9 <= a[i][j] <= ign[i] * d * 1.1:
				# ic += 1
				# s.add(d)
				s[d] = s.get(d, 0) + 1
				d += 1
			d = d0-1
			while d > 0 and ign[i] * d * 0.9 <= a[i][j] <= ign[i] * d * 1.1:
				# s.add(d)
				s[d] = s.get(d, 0) + 1
				d -= 1
		# print(s)
		# lc.append(ic)
		ls.append(s)
	# print(ls)
	s = ls[0]
	rm = set()
	for i in range(len(ls)):
		# si = s.items()
		# lsi = ls[i].items()
		# for j in si & lsi:
		for j in s:
			s[j] = min(ls[i].get(j, 0), s.get(j, 0))
			if s[j] == 0:
				# del s[j]
				rm.add(j)
		for i in rm:
			if i in s:
				del s[i]
	# return min(lc)
	su = 0
	for i in s:
		su += s[i]
	# print(s, su)
	return min(su, p)

def f(n, p, ign, a):
	c = 0
	for j in range(p):
		l = []
		for i in range(n):
			l.append(a[i][j] / ign[i])
		avg = sum(l) / n
		ravg = round(avg)
		# print(avg, ravg)
		d = 0
		for i in range(n):
			if ign[i] * 0.9 <= a[i][j] / ravg <= ign[i] * 1.1:
				d += 1
				print('ser', a[i][j])
		print('d', d)
		if d == n:
			c += 1
	return c

t = int(input())
for it in range(1, t+1):
	n, p = map(int, input().split())
	ign = list(map(int, input().split()))
	a = []
	for i in range(n):
		l = list(map(int, input().split()))
		a.append(l)
	print("Case #%d:" % it, f2(n, p, ign, a))
