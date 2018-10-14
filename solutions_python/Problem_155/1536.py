#

if __name__ == "__main__":
	f = open('qr1.in')
	out = open('qr1.out', 'w')
	nTestCase = int(f.readline().rstrip())
	for testCase in range(nTestCase):
		smax, distributeLevels = f.readline().rstrip().split(' ')
		nStandUp = 0
		nInvited = 0
		nowLevel = 0
		for level in distributeLevels:
			nLevel = int(level)
			if nowLevel > nStandUp:
				nInvited += nowLevel - nStandUp
				nStandUp += nowLevel - nStandUp
			nStandUp += nLevel
			nowLevel += 1
		print "Case #%d: %d\n" % (testCase + 1, nInvited)
		out.write("Case #%d: %d\n" % (testCase + 1, nInvited))

