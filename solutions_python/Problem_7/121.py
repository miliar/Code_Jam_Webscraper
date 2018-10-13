import string
	
a=open("A.in","r")
b=a.readlines()
N=int(b[0])

for caso in range(N):
	triangoli=0
	riga=b[caso+1]
	divisi=string.split(riga," ")
	n=int(divisi[0])
	A=int(divisi[1])
	B=int(divisi[2])
	C=int(divisi[3])
	D=int(divisi[4])
	X=int(divisi[5])
	Y=int(divisi[6])
	M=int(divisi[7])
	punti=range(n)
	punti[0]=[X,Y]
	for i in range(n-1):
		X=(A*X+B)%M
		Y=(C*Y+D)%M
		punti[i+1]=[X,Y]
	for p1 in punti:
		num1=punti.index(p1)
		punti1=punti[(num1+1):len(punti)]
		for p2 in punti1:
			num2=punti1.index(p2)
			punti2=punti1[(num2+1):len(punti1)]
			for p3 in punti2:
				c1=(float(p1[0]+p2[0]+p3[0]))/3
				c2=(float(p1[1]+p2[1]+p3[1]))/3
				if abs(c1-int(c1))+abs(c2-int(c2))==0:
					triangoli+=1
	stringa="Case #"+str(caso+1)+": "+str(triangoli)
	print stringa