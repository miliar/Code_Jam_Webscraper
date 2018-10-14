import sys
def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)
def testcase():
	line = sys.stdin.readline()[:-1]
	# print line
	args = line.split(' ')
	if args[2] == '0' and args[1] != '0':
		return 'Broken'
	if args[2] == '100' and args[1] != '100':
		return 'Broken'
	a = int(args[0])
	b = int(args[1])
	# print '{0}*{1} vs {2}'.format(a, gcd(100, b), b)
	if a*gcd(100,b) >= 100:
		return 'Possible'
	return 'Broken'


line = int(sys.stdin.readline()[:-1])
for i in range(line):
	print 'Case #{0}: {1}'.format(i+1, testcase())
