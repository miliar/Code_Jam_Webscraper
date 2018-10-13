

import sys

if __name__=='__main__':
	input = sys.stdin
	output = open('rezc.txt', 'w')

	t = int(input.readline())
	c = set()
	
	for _t in xrange(t):
		(a, b) = input.readline().strip().split(' ')
		rez = 0
		c = set()
		print len(c)
		for i in xrange(int(a),int(b)+1):
			si = str(i)
			if si in c:
				continue
			perms = [x for x in [si[j:]+si[:j] for j in xrange(1, len(si))] if x>si and x<=b]
			l = len(perms)
			for i in perms:
				if i in c:
					l-=1
				c.add(i)
			rez += (l*(l+1))
		rez/=2
		print len(c), rez
		output.write('Case #%d: %d\n' % (_t+1, rez))
		print a,b
