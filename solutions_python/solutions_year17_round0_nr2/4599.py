def heyy(n):
	for i in range(n, -1, -1):
		j = str(i)
		if ''.join(sorted(j)) == j:
			return j


zz = 1

with open('B-small-attempt0.in') as inputFile, open('B-small-attempt0.out','w') as outputFile:
	for line in inputFile:
		outputFile.write('Case #'+str(zz)+': '+heyy(int(line))+'\n')
		zz += 1