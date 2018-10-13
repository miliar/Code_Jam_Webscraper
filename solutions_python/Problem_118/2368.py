import os
from math import *

f=open("C-small-attempt0.in","r")
r=f.readline()
nb_case = int(r)
r=f.readline()

R=open("resultat.txt","w")

for cases in range(nb_case):
	result=0
	L=r.split(" ")
	for i in range(int(L[0]),int(L[1])+1):
		if (sqrt(i)-int(sqrt(i))==0):
			k=0
			brk=0
			brk2=0
			k2=0
			while k<(len(str(i))):

				if str(i)[k]==str(i)[len(str(i))-1-k]:
					k+=1
				else:
					brk=1
				if k>(len(str(i))/2):
					racine=int(sqrt(i))
					while k2<(len(str(sqrt(i)))):
						if str(racine)[k2]==str(racine)[len(str(int(sqrt(i))))-1-k2]:
							k2+=1
						else:
							brk2=1
						if k2>floor(len(str(int(sqrt(i))))/2)-1:
							result+=1
							brk2=1
							brk=1
						if brk2==1:
							break
				if brk==1:
					break

	r=f.readline()
	R.write("Case #"+str(cases+1)+": "+str(result)+"\n")	


R.close()