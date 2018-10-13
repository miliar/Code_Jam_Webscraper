#!/usr/bin/python2.7
# -*-coding:Utf-8 -*
fich,sor,i=open('B-large.in','r'),open('sortiB.txt','w'),1
T=int(fich.readline())
if T>=1 and T<=400:
	while i<=T:
		g = (fich.readline()).split(" ")
		C,F,X = float(g[0]),float(g[1]),float(g[2])		
		if C>=1 and C<=10000 and F>=1 and F<=100 and X>=1 and X<=100000:
			f,s,gp=2.0,0.0,True
			prev=X/f
			while gp:
				cour=prev
				prev=(C/f)+(X/(f+F))+s
				if prev > cour:
					gp,s=False,s+(X/f)
				else:
					s+=C/f
					f+=F
			s="%.7f"%s #Arrondissment de la valeurs en sortie
			sor.write("Case #"+str(i)+": "+str(s)+"\n")
		i+=1
fich.close()
sor.close()
