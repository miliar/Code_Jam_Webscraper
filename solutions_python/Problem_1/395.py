import sys


def stu(se,qs):
	r = 0
	switchs = 0
	while r < len(qs):
		m = None
		l = None
		for i in se:
			if not i in qs[r:]:
				# print i,"no estaba en",qs[r:]
				return switchs
			
			l = qs[r:].index(i)
			# print "con",i,"recorro",l
			if m == None or l > m:
				m = l
		# print m
		r = r + m
		switchs = switchs + 1
	return switchs
	
	
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	N = int(f.readline())
	
	for c in range(N):
		S = int(f.readline())
		se = []
		for i in range(S):
			se.append( f.readline().strip(' \n\r') );
		Q = int(f.readline())
		qs = []
		for i in range(Q):
			qs.append( f.readline().strip(' \n\r') );
		# print se
		# print qs
		print "Case #%d: %s" % (c+1, stu(se,qs) )
		i = i + 1
	f.close()
