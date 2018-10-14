
fin = '1.in'
fin = 'A-small-attempt0.in'
fin = 'A-large.in'
fout= fin + '.out'

f=open(fin, 'r')
fo=open(fout, 'w')
T = int(f.readline())

for t in range(1, T+1):
	s = f.readline()
	N = int(s.split(' ')[0])
	M = int(s.split(' ')[1])
#	print N, M
	cnt = 0
	st1 = set()
	st1.add('')
	for n in range(1, N+1):
		s = f.readline()
		s = s[0:len(s)-1]
		for it in range(0, s.split('/').__len__()):
			st1.add(s.rsplit('/',it)[0])
	for m in range(1, M+1):
		s = f.readline()
		s = s[0:len(s)-1]
		for it in range(s.split('/').__len__()-1, -1, -1):
			if st1.__contains__(s.rsplit('/',it)[0]):
				pass
			else: 
				st1.add(s.rsplit('/',it)[0])
		#		print 'st1', st1
				cnt+=1
	print 'Case #'+str(t)+ ': '+str(cnt)
	fo.write('Case #'+str(t)+ ': '+str(cnt) + '\n')
