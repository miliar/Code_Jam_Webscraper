a=open('B-large.txt')
o=open('output.txt','w')
T=int(a.readline())
for i in range(1,T+1):
    r=2
    t=0
    inp=a.readline()
    C,F,X=[float(x) for x in inp.split()]
    if X>C:
        t+=(C/r)
        while (X/(r+F))<((X-C)/r):
            r=r+F
            t+=(C/r)
        t+=((X-C)/r)
    else:
        t+=X/r
    o.write('Case #'+`i`+': '+`round(t,7)`+'\n')
    
