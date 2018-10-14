import sys

def calcul(l,taille,k):
    compteur=0
    for i in range(taille):
        if l[i]==0 and i+k<=taille:
            compteur+=1
            for j in range(i,i+k):
                if l[j]==1:
                    l[j]=0
                else:
                    l[j]=1
    for i in range(taille):
        if l[i]==0:
            return(-1)
    return(compteur)




case=1
t=sys.stdin.readline().split()
nb_de_pb=int(t[0])
for p in range(nb_de_pb):
    z="Case #"+str(case)+": "
    case+=1
    l=[]
    t=sys.stdin.readline().split()
    k=int(t[1])
    taille=len(t[0])
    for i in range(taille):
        if t[0][i]=="+":
            l+=[1]
        else:
            l+=[0]
    a=calcul(l,taille,k)
    if a==-1:
        print(z+"IMPOSSIBLE")
    else:
        print(z+str(a))
