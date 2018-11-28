import string
import math


	
f=open('C-small-attempt0.in','r')
tcase=int(f.readline())
ans = 0
for times in xrange(tcase):
	line = f.readline()
	scores = string.split(line)
	a = int(scores[0])
	b = int(scores[1])
	#print a, b
	if a>b:
		#print 'Case #'+str(times+1)+': 0'
		continue
	
	size = math.log(a)/math.log(10)
	if size >= int(size):
		size = int(size)+1

	#print "size ab",size
	#major
	ans=0
	for left in xrange(1, size):
		right = size-left
		#print "LR",left,right
		#print "pair1", max( 1*(10**(left-1)), int(str(a)[:left] )), 1*(10**left) 
		#print "pair2", min(1*(10**right)-1, int(str(b)[:right])), 1*(10**(right-1))-1
		for parl in xrange( max( 1*(10**(left-1)), int(str(a)[:left] )), 1*(10**left) ):
			for parr in xrange( min(1*(10**right)-1, int(str(b)[:right])), 1*(10**(right-1))-1 ,-1 ):
				n = parl*(10**right)+parr 
				m = parr*(10**left)+parl
				#print "aNMb",a,n,m,b
				if n<m:
					if a <= n < m <= b:
						ans = ans + 1
		#print ans
	print 'Case #'+str(times+1)+': '+str(ans)


	
	
	