fp = open('A-small-attempt1.in')
out = open('output.txt','w')
T = int(fp.readline())
casno = 1
while T!=0:
	T-=1
	n1 = int(fp.readline())
	m1 = [map(int,fp.readline().split()) for i in xrange(4)]
	n2 = int(fp.readline())
	m2 = [map(int,fp.readline().split()) for i in xrange(4)]
	r1 = m1[n1-1]
	r2 = m2[n2-1]
	s = set(r1) & set(r2)
	out.write('Case #%d: ' % casno)
	if len(s)==1:
		out.write('%d\n' % list(s)[0])
	elif len(s)>1:
		out.write('Bad magician!\n')
	else:
		out.write('Volunteer cheated!\n')
	casno +=1 