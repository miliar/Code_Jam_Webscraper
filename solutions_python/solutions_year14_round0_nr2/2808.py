R=2

f=input()
fin=open(f, 'r')
T=int(fin.readline().strip())
fout=open("cookie.out", 'w')

for x in range(0, T):
	r=R
	strn=fin.readline().split(" ")
	C=float(strn[0])
	F=float(strn[1])
	X=float(strn[2])
	s=X/r
	while (s>(s-(X/r)+(C/r)+(X/(r+F)))):
		s=s-((X/r)-(C/r)-(X/(r+F)))
		r=r+F
	fout.write("Case #"+str(x+1)+": "+str(round(s,7))+"\n")

