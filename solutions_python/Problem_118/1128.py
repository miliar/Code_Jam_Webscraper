print 'Problem C'

import math
path = r'F:\Dropbox\workspace\GoogleJam'
filNam = 'C-tiny-practice'
filNam = 'C-small-attempt'
#filNam = 'C-large'

inFilNam = '%s\in\%s.in' % (path, filNam)
outFilNam = '%s\in\%s.out' % (path, filNam)

inFile = open(inFilNam, 'r')
outFile = open(outFilNam, 'w')

def isPalindrome(s):
	l = len(s)
	for i in range(math.trunc(l/2)):
		if s[i] <> s[l-1-i]:
			return False
	return True

for count in range(int(inFile.next().strip())):
	[A, B] = [long(s) for s in inFile.next().strip().split(' ')]
	res = 0
	sA, sB = math.sqrt(A), math.sqrt(B)
	tsA, tsB = math.trunc(sA), math.trunc(sB)
	if sA <> tsA: # round up
		tsA += 1
	
	for n in range(tsA, tsB + 1):
		if isPalindrome(str(n)) and isPalindrome(str(n * n)):
			res += 1

	outFile.write('Case #%s: %s\n' % (count + 1, str(res)))

inFile.close()
outFile.close()

print 'Done!'