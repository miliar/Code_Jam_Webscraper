import sys
archivo="asmall.in"
if len(sys.argv)>1:
	archivo=sys.argv[1]

inp=open(archivo)


T=int(inp.readline())
for caso in range(1,T+1):
	A,B,K=[int(s) for s in inp.readline().split(' ')]
	buenos=0
	for i in range(A):
		for j in range(B):
			if i&j<K: buenos+=1
	print "Case #"+str(caso)+":",buenos