mem = {}
def specialRequired(newHeight, initHeight):
	if initHeight <= newHeight:
		return 0
	if (newHeight, initHeight) not in mem:
		mem[(newHeight, initHeight)] = 1 + specialRequired(newHeight, initHeight-newHeight)
	return mem[(newHeight, initHeight)]

for nH in xrange(1, 1001):
	for iH in range(nH+1, 1001):
		specialRequired(nH, iH)

inF = open('small.in')
sol = []
for i in xrange(int(inF.readline())):
	d = int(inF.readline())
	p = map(int, inF.readline().split())
	sol.append(min(newHeight + sum(specialRequired(newHeight, initHeight) for initHeight in p) for newHeight in xrange(1, 1001)))


inF.close()

res = ''
for i in xrange(len(sol)):
	res += "Case #{0}: {1}\n".format(i+1, sol[i])

with open('solution.in', 'w') as solFile:
	solFile.write(res[:-1])