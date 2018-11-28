import math

f = open('1.in','r')
o = open('out.dat','w')

n = int(f.readline())

for i in xrange(n):
	o.write('Case #' + str(i+1) + ': ')
	
	l,p,c = [int(x) for x in f.readline().split()]
	
	a = math.ceil(   math.log(  math.ceil( math.log(1.*p/l,c) ),2  )   )	
	
	o.write(str(int(a)))
	o.write('\n') 
