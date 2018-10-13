x=[1]
for i in range (1,30):
	x.append(x[i-1]*2+1)
r=open('A-small.in','r')
w=open('A-small.out','w')
T=int(r.readline())
n=1
for a in r:
	a=a.split(' ')
	N=int(a[0])
	K=int(a[1])
	int1=K-x[N-1]
	int2=x[N-1]+1
	if K<x[N-1]:
		w.write("Case #{0}: OFF\n".format(n))
	else:
		if (int1 % int2) == 0:
			w.write("Case #{0}: ON\n".format(n))
		else:
			w.write("Case #{0}: OFF\n".format(n))
	n+=1
r.close()
w.close()
