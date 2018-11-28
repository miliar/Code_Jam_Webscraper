fin = open("A-large.in",'r')
f = open("A.out",'w')

flip = {'+':'-','-':'+'}

tt = int(fin.readline())
for t in xrange(tt):
	line = fin.readline()
	cakes,size = [c for c in line.split()[0]],int(line.split()[1])
	operations = 0
	for i in xrange(len(cakes)-size+1):
		if cakes[i]=='-':
			for j in xrange(size):
				cakes[i+j] = flip[cakes[i+j]]
			operations+=1
	if '-' in cakes:
		f.write("Case #{0}: IMPOSSIBLE\n".format(t+1))
	else:
		f.write("Case #{0}: {1}\n".format(t+1,operations))
f.close()
