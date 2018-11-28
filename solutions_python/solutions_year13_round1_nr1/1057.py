import sys,math
PI = math.pi
input = sys.argv[1]
f = open(input,'r')
T = int(f.readline().strip())
for a in range(1,T+1):
	D = [int(x) for x in f.readline().strip().split(" ")]
	r = D[0]
	t = D[1]
	A = float((2*r-1)/4.0)
	#print A
	B = float(t/(2.0))
	#print B
	count  = math.floor((A**2+B)**0.5-A)
	count = int(count)
	#print count
	print "Case #"+str(a)+": "+str(count)

f.close()

