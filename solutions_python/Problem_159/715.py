f=open("A-large.in")
w=open("A-large.out","w")
T=int(f.readline())
for test in range(T):
	N=int(f.readline())
	m=[int(i) for i in f.readline().split()]
	tot=0
	tot2=0
	rate=0
	for i in range(N-1):
		tot+=m[i]-m[i+1] if m[i+1]<=m[i] else 0
		if 0<m[i]-m[i+1]>rate:rate=m[i]-m[i+1]
	for i in range(N-1):
		tot2+=min(m[i],rate)
	w.write("Case #{}: {} {}\n".format(test+1,tot,tot2))
w.close()
