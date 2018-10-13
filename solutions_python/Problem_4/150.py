import string

def prodvett(V1,V2):
	ris=0
	for n in range(len(V1)):
		ris+=V1[n]*V2[n]
	return ris

a=open("A-large.in.txt","r")
b=a.readlines()
T=int(b[0])

for t in range(T):
	n=t*3+2
	v1=b[n]
	v2=b[n+1]
	V1a=string.split(v1," ")
	V2a=string.split(v2," ")
	V1,V2=[],[]
	for i in V1a:
		V1+=[int(i)]
	for i in V2a:
		V2+=[int(i)]
	
	V1.sort()
	V2.sort()
	V2.reverse()
	
	outp="Case #"+str(t+1)+": "+str(prodvett(V1,V2))
	print outp	