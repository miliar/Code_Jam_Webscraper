import itertools as it

def xor(g):
	if len(g)==0:
		return 0
	if len(g)==1:
		return g[0]
	g="^".join([str(i) for i in g])
	return eval(g)

f=open("in.txt")
f_out=open("out.txt","w")
cases=int(f.readline().strip())
for case in range(1,cases+1):
	n=int(f.readline().strip())
	candys=map(int,f.readline().strip().split())
	#print "Candys=:",candys
	m=0
	for r in range(1,n/2+1):
		groups=it.combinations(candys,r)
		for i in groups:
			group1=[j for j in i]
			group2=candys[:]
			for ac in group1:
				group2.remove(ac)
			#print group1,group2, xor(group1),xor(group2)
			if xor(group1)==xor(group2):
				num=max(sum(group1),sum(group2))
				if num>m:
					m=num
	if m==0:
		m="NO"
	f_out.write("Case #%s: %s\n" %(case,m))
