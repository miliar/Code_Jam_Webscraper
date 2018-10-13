T=int(raw_input())
a=0
e=[]
while a<T:
	b=[int(x) for x in raw_input().split()]
	e.append(b)
	a=a+1

a=0
while a<T:
	b=e[a]
	N=b[0]
	R=b[1]
	Y=b[3]
	B=b[5]

	w=0
	if R>N//2 or Y>N//2 or B>N//2:
		w="IMPOSSIBLE"
	
	m=max(R,Y,B)

	if m==R: 
		Z1="R"
		P1=R
		Z2="Y"
		P2=Y
		Z3="B"
	if m==Y: 
		Z1="Y"
		P1=Y
		Z2="R"
		P2=R
		Z3="B"
	if m==B: 
		Z1="B"
		P1=B
		Z2="R"
		P2=R
		Z3="Y"	

	if w==0:
		v=[]
		p=0
		while p<2*P1:
			v.append(Z1)
			v.append("X")
			p=p+2
		while p<N:
			v.append(Z2)
			P2=P2-1
			p=p+1
			if p<N: v.append(Z3)
			p=p+1
		q=1
		while P2>0:
			v[q]=Z2
			P2=P2-1
			q=q+2
		while q<N and v[q]=="X":
			v[q]=Z3
			q=q+2

		w=""
		i=0
		while i<N:
			w=w+v[i]
			i=i+1
			
	q=a+1
	r="Case #"+str(q)+": "+str(w)
	print r
	a=a+1
	



 