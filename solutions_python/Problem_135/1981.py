a=raw_input()
M=[]
Q=[]
for i in range(2*int(a)):
	q  = raw_input()
	v1 = raw_input()
	v2 = raw_input()
	v3 = raw_input()
	v4 = raw_input()
	
	vv1 = v1.split()
	vv2 = v2.split()
	vv3 = v3.split()
	vv4 = v4.split()
	
	T=[vv1,vv2,vv3,vv4]
	Q.append(q)
	matrix=[]
	for i in range(len(T)):
		row= [int(v) for v in T[i]]
		matrix.append(row)
	M.append(matrix)
t=0

for z in range(0,len(M),2):
	A=M[z]
	B=M[z+1]
	n=set(A[int(Q[t])-1])
	m=set(B[int(Q[t+1])-1])
	t+=2
	L=n.intersection(m)
	e=z/2+1
	if len(L)==0:
		print 'Case #%i: Volunteer cheated!' %e
	if len(L)==1:
		print 'Case #%i: %i' %(e,n.intersection(m).pop())
	if len(L)>1:
		print 'Case #%i: Bad magician!' %e
