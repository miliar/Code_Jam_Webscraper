import sys
with open(sys.argv[1]) as fp:
    T=int(fp.readline())
    def Recycle(A,B):
	rotate = lambda n,r: n[r:]+n[:r]
	_str,_int,_range,_len=str,int,range,len
        return len({(n,rotate(_str(n),i)) for n in range(A,B+1) for i in _range(len(_str(n))) if A<=n<_int(rotate(_str(n),i))<=B})
    for i in range(1,T+1):
        A,B=map(int,fp.readline().split())
        print "Case #{0}: {1}".format(i,Recycle(A,B))
