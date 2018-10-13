print 'Problem B'

path = r'F:\Dropbox\workspace\GoogleJam'
filNam = 'B-tiny-practice'
filNam = 'B-small-attempt'
filNam = 'B-large'

inFilNam = '%s\in\%s.in' % (path, filNam)
outFilNam = '%s\in\%s.out' % (path, filNam)

inFile = open(inFilNam, 'r')
outFile = open(outFilNam, 'w')

def lowerOrEqual(x, list):
	for el in list:
		if el > x:
			return False
	return True

def isValid(grass):
	for list in grass:
		for el in list:
			if el > 100 or el < 1:
				return False
	return True

def exists(N, M, grass, tgrass):
	for i in range(N):
		for j in range(M):
			x = grass[i][j]		
			if not (lowerOrEqual(x, grass[i]) or lowerOrEqual(x, tgrass[j])):
				return 'NO'
	return 'YES'
			
lcount = int(inFile.next().strip())
for count in range(lcount):
	[N, M] = [int(s) for s in inFile.next().strip().split(' ')]
	grass, tgrass = [], []
	for _ in range(N):
		grass.append([int(s) for s in inFile.next().strip().split(' ')])

	for i in range(M):
		tgrass.append([grass[j][i] for j in range(N)])
	
	if isValid(grass):
		res = exists(N, M, grass, tgrass)
	else:
		res = 'NO'

	outFile.write('Case #%s: %s\n' % (count + 1, str(res)))

inFile.close()
outFile.close()

print 'Done!'