filename = 'A-large.in'
f = open(filename,'r')

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t, 
	D,N = map(int,f.readline().split())
	t = 0
	for i in range(N):
		k,s=map(int,f.readline().split())
		t = max(t,(D-k)/float(s))
	print (D/t)
