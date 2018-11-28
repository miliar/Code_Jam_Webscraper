def str2list(t):
    d=len(t)-1
    t=t+' '
    d=len(t)-1
    b=0
    g=[]
    z=0
    while b<=d:
        if t[b]==' ':
            g.append(float(t[z:b]))
            z=b
        b+=1
    return g
f=open('C:/Users/Administrateur/Desktop/t.txt','r')
t=f.readlines()
f.close()
g=lambda x:x[0:-1]
for i in range(0,len(t)):
    t[i]=g(t[i])
    t[i]=str2list(t[i])
c=t[0][0]
s=2
gttt=0
for i in range(1,int(c+1)):
    gc=t[i][0]
    gf=t[i][1]
    gx=t[i][2]
    gt=gx/s
    gtt=gc/s
    while (gtt+(gx/(s+gf)))<gt:
        gttt=gttt+gtt
        s=s+gf
        gt=gx/s
        gtt=gc/s

    gttt=gttt+gt
    print 'Case #%d: %0.7f' %(i,gttt)
    s=2
    gttt=0