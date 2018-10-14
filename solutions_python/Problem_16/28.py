import sys
def runlength(s):
	last = s[0]
	groups = 1
	for i in s[1:]:
		if i != last:
			last = i
			groups +=1 
	return groups
		
def permutations(l,callback,sf=None):
	if sf == None: sf = []
	
	if l == []:
		callback(sf)
	
	for i in l:
		l1 = l[:]
		l1.remove(i)
		permutations(l1,callback,sf+[i])

def applyperm(perm,s):
	global maxrl
	
	l = [' '] * len(s)
	for i in xrange(0,len(s),len(perm)):
		for j,k in enumerate(perm):
			l[i+k] = s[i+j]
	news = ''.join(l)
	newrl = runlength(news)
	if newrl < maxrl:
		maxrl = newrl
			


N = int(raw_input())

for case in xrange(1,N+1):
	k = int(raw_input())
	s = raw_input()
	
	maxrl = len(s)
	permutations(range(k),lambda x: applyperm(x,s))
	print "Case #%d: %d" % (case, maxrl)	