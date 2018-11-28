from sys import stdin
def comprobacion(n,wea):
    if wea==False:
        n=int(''.join(map(str,n)))

    n=str(n)
    a=len(n)
    comp=True
    if (n[0] <= n[a-1]) :
        for z in range (0,a-1):
            if n[z] <= n[z+1] :
                comp=comp and True
            else :
                comp=comp and False
                break
    else :
        comp=False
    return comp

def problemsolver(n):
    cambio = False
    m = list(n)
    for i in range(0, len(m)-1):
        cambio = False
        if int(m[i]) > int(m[i+1]):
            m[i] = str(int(m[i])-1)
            for c in range(i,len(m)-1):
                m[c+1] = "9"
                cambio = True
        if cambio ==True :
            break

    return m

t=stdin.readline().strip()
t=int(t)

for x in range(0,t):
    wea=True
    n=stdin.readline().strip()
    a=(problemsolver(n))
    num = int(''.join(map(str,a)))
    j=comprobacion(num,wea)
    while j==False:
        a=problemsolver(a)
        wea=False
        j=comprobacion(a,wea)
    num = int(''.join(map(str,a)))
    print("Case #"+str(x+1)+": "+str(num))