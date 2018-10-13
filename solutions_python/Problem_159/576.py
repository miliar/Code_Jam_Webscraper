def firstMethod(onPlate):
	res = 0
	for i in xrange(1, len(onPlate)):
		res += max(0, onPlate[i-1] - onPlate[i])
	return res

def secondMethod(onPlate):
	rate = 0
	for i in xrange(1, len(onPlate)):
		rate = max(rate, onPlate[i-1] - onPlate[i])
	res = 0
	for i in xrange(len(onPlate)-1):
		res += min(onPlate[i], rate)
	return res

sol = []

inF = open('asmall.in')
for case in xrange(int(inF.readline())):
	N = int(inF.readline())
	onPlate = map(int, inF.readline().split())
	sol.append('%i %i' % (firstMethod(onPlate), secondMethod(onPlate)))

inF.close()
res = ''
for i in xrange(len(sol)):
	res += "Case #{0}: {1}\n".format(i+1, sol[i])

with open('solution.in', 'w') as solFile:
	solFile.write(res[:-1])