from unionfind import *
def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

pr=primes(1001)
for case in range(input()):
    print "Case #"+str(case+1)+":",
    A,B,P=map(int,raw_input().split())
    allsets=[[x] for x in range(A,B+1)]
    uf=UnionFind()
    uf.insert_objects(range(A,B+1))
    for j in pr:
        if j<P: continue
        if j>(B-A+1): break
        for i in range((1+(A-1)/j)*j,B,j):
            if (i+j)>B: break
            uf.union(i,i+j)
            #print allsets
            #i1=[(i+j in y) for y in allsets].index(True)
            #i2=[(i in y) for y in allsets].index(True)
            #allsets[i1] += allsets[i2]
            #allsets.pop(i2)
    #print len(allsets)
    print str(uf).count("[")
