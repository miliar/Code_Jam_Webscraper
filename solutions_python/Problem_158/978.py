infile = open('B-small-attempt8.in', 'r')
outfile = open('out.txt', 'w')

def constfn(i):
	return ((2**i) - 1)
def groupfn(n, i):
	return (n/(2**i)) + (n&1)

n = int(infile.readline().strip()) # Number of test cases

for i in xrange(n):
	d = int(infile.readline().strip())
	P = [int(x) for x in infile.readline().strip().split()]
	ihop = [[x,0,0,x] for x in P] #[n, i, c, g]

	group = max( [x[3] for x in ihop] )
	constant = 0

	while True:
		# Find bottleneck
		for j in xrange(d):
			if j == 0:
				slow = j
				g = ihop[j][3]
				continue
			if ihop[j][3] > g:
				g = ihop[j][3]
				slow = j

		# Test for improvement
		for j in xrange(d):
			if ihop[j][3] == g:
				ihop[j][1] += 1
				ihop[j][2] = constfn(ihop[j][1])
				ihop[j][3] = groupfn(ihop[j][0], ihop[j][1])
		
		newgroup = max( [x[3] for x in ihop] )
		newconstant  = sum( [x[2] for x in ihop] )
		
		if (group + constant) < (newconstant + newgroup):
			break
		else:
			group = newgroup
			constant = newconstant

	print 'Case #%d: %d' % (i+1, (group + constant))
	outfile.write('Case #%d: %d\n' % (i+1, (group + constant)))
	#print i
	#print P
	#print '%d' % ((group + constant))
	#print ''

infile.close()
outfile.close()
