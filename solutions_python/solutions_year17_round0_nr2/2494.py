f = open('B-large.in', 'r')
g = open('tidy_output.txt', 'w')

def get_offender(narray):
	l = len(narray)	
	offender = -1
		
	for x in xrange(1,l):
		if narray[x] < narray[x-1]:
			offender = x
			
	return offender
	
def straighten(narray, offender):	
	return narray[:offender-1] + [narray[offender-1]-1] + [9] * (len(narray) - offender)
	
def wash(narray):
	start = 0
	while narray[start] == 0:
		start += 1
	return ''.join(str(x) for x in narray[start:])

t = int(f.readline())
for case in xrange(t):
	n = int(f.readline())
	narray = map(int, str(n))
	
	offender = get_offender(narray)
	while offender > -1:
		narray = straighten(narray, offender)		
		offender = get_offender(narray)
		
	outfirst = 'Case #' + str(case+1) + ': '
	outmid = wash(narray)
	outlast = '\n' if case < t-1 else ''
	
	g.write(outfirst + outmid + outlast)