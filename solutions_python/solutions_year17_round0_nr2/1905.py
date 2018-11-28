def lire(path) :
    test = open(path, "r")
    liste = []
    long = int(test.readline())
    for c in test.readlines():
        ligne = c.rstrip()
        liste.append(ligne)
    test.close()
    return liste

def decomp(nb):
    li = []
    while nb!=0: 
        li.append(nb%10)
        nb//=10
    return(li[::-1])

def comp(x):
    if x =="+" :
        return "-"
    else :
        return "+"
    
def inv(fin, ch, larg):
    for i in range(larg):
        ch[fin-i] = comp(ch[fin-i])
    return ch
def bon(ch):
    for c in ch:
        if c =="-":
            return False
    return True

def recomp(li) :
    s  = 0
    n = len(li)
    for i in range(n):
        s += li[i] * 10**(n-i-1)

    return s

def est_tidy(li):
    if li == [0] :
        return False
    for i in range(1,len(li)) :
        if li[i]<li[i-1] :
            return False
    return True

# nb_tidy(n):
 ##   for i in range(n):
 ##       if est_tidy(n-i):
 #          return n-i
        
def nb_tidy(n):
    li = decomp(n)
    i = len(li)-1
    while not(est_tidy(li)):
        li[i] =9
        li[i-1] -= 1
        i -= 1
    return recomp(li)
        
        
        

def main():
    liste = lire("B-large.in.txt")
    print(liste)
    rep = open("B_large_0", "w")
    cas = 1
    for m in liste :
        rep.write("Case #" + str(cas)+": " + str(nb_tidy(int(m)))+"\n")
        cas+=1

    rep.close()
    
