fin = open('A-large-0.in','r')
fout = open('A-large-0.out','w')

n = int(fin.readline())
for i in range(1,n+1):
	x = 0
	read = fin.readline().split()
	S = int(read[0])
	P = str(read[1])
	T = 0
	for j in range(0,S+1):
		if int(P[j]) > 0:
			T += int(P[j])
			if T <= j:
				x += j-T
				T = j
		else:
			if T <= j:
				x += 1
				T += 1
	fout.write("Case #%d: %d\n" % (i, x))
fin.close()
fout.close()