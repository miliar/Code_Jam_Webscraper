from sys import stdin
def gatito(n):
    change = False
    lista = list(n)
    for i in range(0, len(lista)-1):
        change = False
        if int(lista[i]) > int(lista[i+1]):
            lista[i] = str(int(lista[i])-1)
            for c in range(i,len(lista)-1):
                lista[c+1] = "9"
                change = True
        if change ==True :
            break

    return lista
    
def works(n,boolq):
    if boolq==False:
        n=int(''.join(map(str,n)))

    n=str(n)
    a=len(n)
    help4=True
    if (n[0] <= n[a-1]) :
        for i2 in range (0,a-1):
            if n[i2] <= n[i2+1] :
                help4=help4 and True
            else :
                help4=help4 and False
                break
    else :
        help4=False
    return help4



t=stdin.readline().strip()
t=int(t)

for x in range(0,t):
    boolq=True
    n=stdin.readline().strip()
    a=(gatito(n))
    aiuda = int(''.join(map(str,a)))
    PL=works(aiuda,boolq)
    while PL==False:
        a=gatito(a)
        boolq=False
        PL=works(a,boolq)
    aiuda = int(''.join(map(str,a)))
    print("Case #"+str(x+1)+": "+str(aiuda))