fin=open('A-small-attempt0.in')
fout=open('A.out','w')
T=int(fin.readline())
for i in xrange(0,T):
	l={}
	for j in range(0,17):
		l[str(j)] = 0
	a1=int(fin.readline())
	t=[]
	for j in xrange(0,4):
		t.append(fin.readline().strip())
	for j in t[a1-1].split(' '):
		l[j] = l[j] + 1
	a2=int(fin.readline())
	t=[]
	for j in xrange(0,4):
		t.append(fin.readline().strip())
	for j in t[a2-1].split(' '):
		l[j] = l[j] + 1
	found = 0
	for (k,v) in l.items():
		if v == 2 and found == 0:
			found = int(k)
		elif v == 2 and found > 0:
			found = -1
	if found == 0:
		fout.write('Case #%d: Volunteer cheated!\n' % (i+1))
	elif found == -1:
		fout.write('Case #%d: Bad magician!\n' % (i+1))
	else:
		fout.write('Case #%d: %d\n' % (i+1,found))
fout.close()
