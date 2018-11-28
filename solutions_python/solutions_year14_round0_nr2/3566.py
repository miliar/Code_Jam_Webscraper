from math import *
filen = 'B-small-attempt2'
with open(filen + '.in') as inp:
	arrs = [[float(elem.strip('\n')) for elem in inp.next().split(' ')]for x in xrange(int(inp.next()))]
#arr = [case1, case2, case3...] where casen = [cost of cookie farm, increase in rate, tot needed]
ans = []
for arr in arrs:
	c = float(arr[0])
	f = float(arr[1])
	x = float(arr[2])
	caseans = [x / 2.0]
	n = 1
	while True:
		caseans.append(x / (2 + f * n) + sum([c / (2 + i * f) for i in xrange(n)]))
		if caseans[n] > caseans[n - 1]:
			break
		n += 1
	ans += [min(caseans)]
print ans
ans = '\n'.join(["Case #%d: "%(x + 1) + str(ans[x]) for x in xrange(len(ans))])
with open(filen +'.out','w') as outp:
	outp.write(ans)