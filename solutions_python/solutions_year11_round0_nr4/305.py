import sys

sinfile = sys.argv[1]
soutfile = sinfile[:-2] + 'out'

finfile = open(sinfile)
foutfile = open(soutfile, 'w')


n = int(finfile.readline().strip())

def diff(arr):
	init = 1
	o = []
	for x in arr:
		o.append(abs(x-init))
		init = x
	return o

for i in range(1, n+1):
	cases = finfile.readline().strip()
	numbers = finfile.readline().strip().split(' ')
	
	j = 1
	ans = 0
	for k in numbers:
		if j != int(k):
			ans += 1
		j+=1

	print >> foutfile, ('Case #%d: %s' % (i, ans)).replace("'", '')