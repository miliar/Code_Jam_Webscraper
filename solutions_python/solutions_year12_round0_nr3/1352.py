import sys

#entrada = sys.argv[1]


def rcn(num,n,m):
	s = set()
	#print num
	res = 0
	sz = len(str(num))
	snum = str(num) + str(num)
	for i in xrange(1,sz):
		tnum = snum[i:i+sz]
		#print ' ' + str(tnum)
		if int(tnum)>n and int(tnum) <= m and int(tnum)!=num:
			#print ' ' + str(tnum)
			if not int(tnum) in s:
				res += 1
				s.add(int(tnum))
	return res

fin = open('C-large.in',"r")

N = int(fin.readline().strip())

for i in xrange(1,N+1):
	res = 0
	linea = fin.readline()
	n,m = map(int,linea.strip().split())
	for j in xrange(n,m+1):
		res += rcn(j,j,m)		

	print 'Case #' +str(i) + ': ' + str(res) 
