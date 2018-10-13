# -*- coding: utf-8 -*-


def sep(chaine): #recupere les elements de la chaine separes par des espaces    
    liste=[]
    c=0
    n=len(chaine)
    while c<>n-1:
      k=c
      while k<>n-1 and chaine[k]<>' ':
	k=k+1
      if k<>n-1:	
       liste.append(chaine[c:k])
       c=k+1
      else:
	liste.append(chaine[c:n])
	c=n-1
    return liste    
    
    
def conversion(liste) :    #convertit une liste de chaine de caracteres en une liste d'entiers
    L=[]
    for k in range(0,len(liste)):
      L.append(int(liste[k]))
    return L  
 
 
def nbclap(listeSi):
  k=0
  n=1
  S=0
  while n<>0:
    arret=min([S+1,len(listeSi)])
    a=S
    for l in range(k,arret):
      S=S+listeSi[l]
    k=arret
    if k==len(listeSi):
	n=0
    else:
	n=S-a
  return S

def nbzeros(liste,depart):
  k=depart
  while k<len(liste) and liste[k]==0:
    k=k+1
  return (k-depart)  


def nbinvites(listeSi):
  S=0
  L=[listeSi[k] for k in range(0,len(listeSi))]
  N=sum(L[a] for a in range(0,len(L)))
  n=0
  while S<>N:
    S=nbclap(L)
    b=nbzeros(L,S)
    n=n+b
    L[0]=L[0]+b
    N=N+b
  return n
    


#print(nbinvites([1,1,0,0,1,1]))

#print(nbinvites([2,0,0,2,0,0,1]))
#print(nbclap([5,0,0,2,0,0,1]))
 
finput=open('exemple.txt','r')
foutput=open('reponses.txt','w')
    
    
L=finput.readlines()
r=1
for l in L[1:]:
  listeSi=[int(sep(l)[1][k]) for k in range(0,len(sep(l)[1])-1)]
  n=nbinvites(listeSi)
  foutput.write('Case #'+str(r)+': '+str(n)+'\n')
  r=r+1
 

 
finput.close()
foutput.close()

