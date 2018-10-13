def lire(path) :
    test = open(path, "r")
    liste = []
    long = int(test.readline())
    for c in test.readlines():
        ligne = c.rstrip()
        liste.append(list(map(int, ligne.split())))
    test.close()
    return liste

def dichot(L,i,j,X):
    if X>L[j]:
        return j+1
    while i!=j:
        k=(i+j)//2
        if X<=L[k]:
            j=k
        else:
            i=k+1
    return i
 
def inserer(a, L):
    if L == [] :
        return [a]
    k=dichot(L,0,len(L)-1,a)
    L.insert(k,a)
    return L

def p_parmi_n(p,n):
    espaces = [n]
    for i in range(p):
        maxi = espaces.pop()
        if maxi%2 ==0 :
            espaces=inserer((maxi-1)//2 +1, espaces)
            espaces=inserer((maxi-1)//2, espaces)
            rep = [(maxi-1)//2 +1, (maxi-1)//2 ]
        else :
            espaces=inserer( (maxi-1)//2 , espaces)
            espaces=inserer( (maxi-1)//2, espaces)
            rep = [(maxi-1)//2 ,(maxi-1)//2 ]
        #print(espaces)
    return rep

def main():
    liste = lire("C-small-1-attempt0.in.txt")
    print(liste)
    rep = open("C_small_0", "w")
    cas = 1
    for m in liste :
        maxi, mini = p_parmi_n(m[1],m[0])
        rep.write("Case #" + str(cas)+": " + str(maxi)+" "+str(mini)+"\n")
        cas+=1

    rep.close()
    


    
