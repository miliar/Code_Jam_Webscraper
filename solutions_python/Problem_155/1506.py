sol = []
inF = open('A-large.in')
for case in xrange(int(inF.readline())):
	sM, s = inF.readline().split()
	sM, s = int(sM), map(int, s)
	needed = 0
	soFar = s[0]
	for i in xrange(1, sM+1):
		needed = max(needed, i-soFar)
		soFar += s[i]
	sol.append(needed)

inF.close()

res = ''
for i in xrange(len(sol)):
	res += "Case #{0}: {1}\n".format(i+1, sol[i])

with open('solution.txt', 'w') as solFile:
	solFile.write(res[:-1])
