def on_off(N, K):
	"""docstring for on_off"""
	for i in range(0,N):
		if (K / 2**i) % 2 == 0:
			return 'OFF'
	return 'ON'


fin = open('A-large.in', 'r')
data = fin.readlines()
fin.close()
fout = open('A-large.out', 'w')
for i in range(1,len(data)):
	nk = data[i].split()
	n = int(nk[0])
	k = int(nk[1])
	fout.write('Case #{0}: {1}\n'.format(i,on_off(n,k)))
fout.close()
