filename = 'C-large.in'
f = open(filename,'r')

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t ,
	N,K = map(int,f.readline().split())
	kb = len(bin(K)) - 2
	a = 2**(kb-1)
	x = ((N - (a-1)) / a) + ((K-a) < (N-(a-1)) % a)
	print x/2 , x/2 - (x-1)%2