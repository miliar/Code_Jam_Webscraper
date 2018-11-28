'''
Created on May 8, 2010

@author: qfel13
'''

if __name__ == '__main__':
	f = open("C-small-attempt0.in", "r")
	fout = open("C-small.out", "w")
	caseCount = int(f.readline())
	for case in xrange(caseCount):
		a = f.readline().split(" ")
		r = int(a[0])
		k = int(a[1])
		n = int(a[2])
		gstr = f.readline().split(" ")
		g = []
		for gi in gstr:
			g.append(int(gi))
#		print r, k, n
#		print g
		sum = 0
		i = 0
		for ri in xrange(r):
			partsum = 0
			l = 0
			while partsum + g[i] <= k and l < n:
#				print "partsum", partsum
#				print "i", i
#				print "g[i]", g[i]
#				print "partsum + g[i]", partsum + g[i]
				partsum += g[i]
				l += 1
				if i < n - 1:
					i += 1
				else:
					i = 0
			sum += partsum
		fout.write("Case #" + str(case + 1) + ": " + str(sum) + "\n")
#		print "Case #" + str(case + 1) + ": " + str(sum)