import sys

f = open(sys.argv[1],'r')
T = int(f.readline())

for t in range(T):
	N = int(f.readline())
	l = [int(x) for x in f.readline().strip().split()]
	tot = 0
	for i in l:
		tot ^= i
	if tot:
		print 'Case #%d: NO' %(t+1)
	else:
		print 'Case #%d: %d' %((t+1), sum(l) - min(l))
