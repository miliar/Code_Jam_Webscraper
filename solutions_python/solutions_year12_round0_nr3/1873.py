def is_recycled_pair(n,m):
	if n>=m:
		return False
	else:
		n1=str(n)
		n2=str(m)
		for i in range(len(n1)):
			n1=n1[-1]+n1[:-1]
			if n1==n2:
				return True
def recycled_number(a,b):
	count=0
	for i in range(b,a,-1):
		m=i
		for j in range(a,i):
			if is_recycled_pair(j,m):
				count=count+1
	return count
o=open("C-small-attempt6.in","r")
r=o.readlines()
w=open("C.out","w")
r=r[1:]
case=0
for i in r:
	n=i.split()
	a=int(n[0])
	b=int(n[1])
	c=recycled_number(a,b)
	case=case+1
	#w.write("Case #%d:%d\n"%(case,c))
	if case==50:
		w.write("Case #%s: %s"%(case,c))
	else:
		w.write("Case #%s: %s\n"%(case,c))

w.close()
o.close()
