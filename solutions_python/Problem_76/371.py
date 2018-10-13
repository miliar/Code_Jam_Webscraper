import sys
import math

sinfile = sys.argv[1]
soutfile = sinfile[:-2] + 'out'

finfile = open(sinfile)
foutfile = open(soutfile, 'w')

def splitlist(thelist):
	'''assuming empty sets are not permitted....'''
	llen = len(thelist)
	maxpossiblecase = int("1" * llen, 2)
	half = math.ceil( maxpossiblecase / 2. )
	i = 0
	while i < half:
		i+=1
		bools = list(bin(i)[2:].zfill(llen))
		a = []
		b = []
		for x in range(len(bools)):
			if bools[x] == '0':
				a.append(thelist[x])
			else:
				b.append(thelist[x])
		yield (a, b)
		
def wrongsum(thelist):
	return reduce(lambda x, y: x^y, thelist)
	
n = int(finfile.readline().strip())

for i in range(1, n+1):
	finfile.readline() # ignore?
	thelist = finfile.readline().strip().split(' ')
	thelist = map(int, thelist)
	
	#ans = "NO"
	ans = 0
	for cases in splitlist(thelist):
		f = cases[0]
		s = cases[1]
		if wrongsum(f) == wrongsum(s):
			ans = max(ans, max(sum(f), sum(s)))

	if ans == 0:
		ans = "NO"
	print >> foutfile, ('Case #%d: %s' % (i, ans))