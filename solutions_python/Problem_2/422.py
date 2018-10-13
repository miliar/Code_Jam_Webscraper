import string

def converti(matrice,t):
	opp=[]
	opa=[]
	for i in matrice:
		op1=string.split(i," ")
		op2=string.split(op1[0],":")
		opp+=[int(op2[0])*60+int(op2[1])]
		op3=string.split(op1[1],":")
		opa+=[int(op3[0])*60+int(op3[1])+t]
	return opp,opa

def ordina(m):
	pro=m[0]
	for k in range(len(pro)):
		if k>0:
			if pro[k] in pro[0:k-1]:
				pro[k]+=0.01
	mo=sorted(pro)
	ma=m[1]
	mo2=range(len(mo))	
	for i in range(len(mo)):
		b=m[0].index(mo[i])
		mo2[i]=ma[b]
	for i in range(len(mo)):
		mo[i]=int(mo[i])

	return mo,mo2

a=open("B-small-attempt1.in","r")
b=a.readlines()
N=int(b[0])
riga=1

for caso in range(N):
	T=int(b[riga])
	[NA,NB]=string.split(b[riga+1]," ")
	NA,NB=int(NA),int(NB)
	ab,ba=[],[]
	for x in range(NA):
		ab+=[b[riga+2+x][:-1]]
	for x in range(NB):
		ba+=[b[riga+2+x+NA][:-1]]
	mab=converti(ab,T)
	mba=converti(ba,T)

	nab=ordina(mab)
	nba=ordina(mba)

	treni_a=0
	treni_b=0
	
	num_ta=0
	num_tb=0

	for tempo in range(1440):
		for l in range(len(nab[0])):
			arrivob=nab[1][l]
			if tempo==arrivob:
				treni_b+=1
		for l in range(len(nba[0])):
			arrivoa=nba[1][l]
			if tempo==arrivoa:
				treni_a+=1
		for l in range(len(nab[0])):
			partenzaa=nab[0][l]
			if tempo==partenzaa:
				treni_a-=1
				if treni_a==-1:
					treni_a+=1
					num_ta+=1
		for l in range(len(nba[0])):
			partenzab=nba[0][l]
			if tempo==partenzab:
				treni_b-=1
				if treni_b==-1:
					treni_b+=1
					num_tb+=1

	outp="Case #"+str(caso+1)+": "+str(num_ta)+" "+str(num_tb)
	print outp

	riga+=2+NA+NB
