import string 

T = int(raw_input())

def hfill(R, C, a):
	for i in xrange(R) :
		j = 0
		while j<C and a[i][j] =='?' : j+=1
		if j<C :
			current = a[i][j]
			for k in xrange(j) : a[i][k] = current 
			for k in xrange(j+1, C):
				if a[i][k] == '?' : a[i][k] = current
				else : current = a[i][k]


def vfill(R, C, a):
	for i in xrange(C) :
		j = 0
		while j<R and a[j][i] =='?' : j+=1
		if j<R :
			current = a[j][i]
			for k in xrange(j) : a[k][i] = current 
			for k in xrange(j+1, R):
				if a[k][i] == '?' : a[k][i] = current
				else : current = a[k][i]
		  
for test in xrange(T):
	R, C =  map(int, raw_input().split())
	a = []
	for _ in xrange(R): a.append(list(raw_input())) 
	hfill(R,C,a)
	vfill(R,C,a)
	print "Case #%d:"%(test+1)    
	for i in xrange(R): print ''.join(a[i])
		
	
