f = open('1.in','r')
o = open('out.dat','w')

n = int(f.readline())

for i in xrange(n):
	N,K = f.readline().split()
	N = int(N)
	K = int(K)
	
	a = (K + 1) % 2**N
	
	if a:
		o.write('Case #' + str(i+1) + ': '+ 'OFF' +'\n')
	else:
		o.write('Case #' + str(i+1) + ': '+ 'ON' +'\n')
