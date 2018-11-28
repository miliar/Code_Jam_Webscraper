print 'Problem XXX'

import math
problemRef = 'A'
path = r'F:\Dropbox\workspace\GoogleJam'
filNam = problemRef + '-tiny-practice'
filNam = problemRef + '-small-attempt0'
#filNam = problemRef + '-large'

inFilNam = '%s\in\%s.in' % (path, filNam)
outFilNam = '%s\in\%s.out' % (path, filNam)

inFile = open(inFilNam, 'r')
outFile = open(outFilNam, 'w')

lcount = int(inFile.next().strip())
for count in range(lcount):
	[r, t] = [long(s) for s in inFile.next().strip().split(' ')]

	res = 0
	done = False
	while  t >= 0 and not done:
		s = 2.0 * r + 1.0 #(r + 1) * (r + 1) - (r * r)
		if t >= s:
			res += 1
			t = t - s
			r += 2.0
		else:
			done = True
	#print res
	
	outFile.write('Case #%s: %s\n' % (count + 1, str(res)))

inFile.close()
outFile.close()

print 'Done!'