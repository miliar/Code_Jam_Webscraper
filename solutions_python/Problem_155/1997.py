import sys

lines = [line.strip('\n') for line in open(sys.argv[1], 'r')]
fOut = open(sys.argv[2], 'w')

cases = int(lines[0]);
for case in range(1, cases + 1):
	splitLine = lines[case].split(' ')
	
	sMax = int(splitLine[0])
	s = [int(x) for x in splitLine[1]]
	
	amount = 0
	needed = 0
	
	for i in range(sMax + 1):
		needed += max(0, i - amount - needed)
		amount += s[i]
	
	fOut.write('Case #%s: %s\n' % (case, needed))

fOut.close()
print 'Done.'