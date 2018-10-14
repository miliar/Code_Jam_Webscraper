f = open('recycled.in', 'r')
out = open('recycled.out', 'w')

t = int(f.readline().strip())
for T in xrange(1, t+1):
	ans = 0
	out.write('Case #%s: ' % T)
	a, b = [int(x) for x in f.readline().split()]
	for i in xrange(a, b+1):
		seen = {}
		tmp = str(i)
		for j in xrange(len(tmp)):
			s = tmp[j]
			k = (j+1) % len(tmp)
			while k != j:
				s += tmp[k]
				k = (k+1) % len(tmp)
			if int(s) > i and int(s) <= b and str(int(s)) == s and s not in seen:
				ans += 1
				seen[s] = True
	out.write('%s\n' % ans)

f.close()
out.close()