import math
f = open('input.txt','r')
w = open('output.txt','w')
nmax=int(f.readline())
for n in range(0,nmax):
    l=f.readline().split()
    C=float(l[0])
    F=float(l[1])
    X=float(l[2])
    m=int(math.ceil((F*X-F*C-2*C)/(C*F)))
    m=max(m,0)
    t=0
    for M in range(0,m):
        t+=C/(2+F*M)
    t+=X/(2+F*m)
    w.write('Case #'+str(n+1)+': '+str(t)+'\n')
f.close()
w.close()
