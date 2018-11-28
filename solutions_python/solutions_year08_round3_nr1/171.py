import sys
import math

def minkey(p,k,l,f):
	
	f.sort()
	f.reverse()
	# print len(f),l
	r = 0
	t = 1
	i = 0
	for z in range(p):
		for j in range(k):
			# print i
			if i == l:break
			r = r + f[i]*t
			i = i + 1
		t = t + 1


	return r
	
if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	N = int(f.readline())
	
	for c in range(N):
		d = f.readline().strip(' \n\r').split(' ')
		P,K,L = map(lambda f: int(f),d)
		F = f.readline().strip(' \n\r').split(' ')
		F = map(lambda f: int(f),F)
		
		print "Case #%d: %d" % (c+1, minkey(P,K,L,F))
	f.close()
