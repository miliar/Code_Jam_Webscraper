from math import *
inf = open("file.in")
ouf = open("file.out","w")
counttests = int(inf.readline().split()[0])
case = 0
def answer(x):
	global case, counttests
	if case > counttests:
		exit
	case += 1
	print "Case #"+str(case)+": "+str(x)
	print >>ouf, "Case #"+str(case)+": "+str(x)

for iii in xrange(counttests):
	n,m = map(int,inf.readline().split())
	res = 0
	s = set([])
	for i in xrange(n):
		st = inf.readline()
		tek = 1
		s |= set([st[:-1]])
		while st.find('/',tek)!= -1:
			tek=st.find('/',tek)
			s |= set([st[:tek]])
			tek += 1
	for i in xrange(m):
		st = inf.readline()
		tek = 1
		while st.find('/',tek)!= -1:
			tek=st.find('/',tek)
			if st[:tek] in s:
				pass
			else:
				res += 1;
			s |= set([st[:tek]])
			tek += 1
		if st[:-1] in s:
			pass
		else:
			res += 1
		s |= set([st[:-1]])
	answer(res)
