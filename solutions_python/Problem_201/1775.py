from sys import stdin


def placement(liste,L):#liste contient les positions occupees,L les nombres de places libres
    #L=[]
    #for i in range(1,len(liste)):
    #    L.append(liste[i]-liste[i-1]-1)
    m = max(L)
    k=0
    while k< len(L) and L[k]!=m :
        k+=1
    liste.append(liste[k]+(m-m//2))
    liste.sort()
    L[k]=m-m//2-1
    L.insert(k+1,m//2)
    return (m-m//2-1,m//2)


def answer(c):
    l = c.split()
    N = int(l[0])
    K = int(l[1])
    liste = [0,N+1]
    L=[N]
    for k in range(K):
        (x,y)=placement(liste,L)
    return str(y)+' '+str(x)

T = int(stdin.readline())
for case in range(1,T+1):
    c = stdin.readline()
    print('Case #%i: %s' % (case,answer(c)))






