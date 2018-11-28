def str2list(t):
    d=len(t)-1
    t=t+' '
    d=len(t)-1
    b=0
    g=[]
    z=0
    while b<=d:
        if t[b]==' ':
            g.append(int(t[z:b]))
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
k=1
s=0
gf=0
for i in range(1,c+1):
    d=t[t[k][0]+k]
    b=t[t[k+5][0]+k+5]
    for j in range(0,4):
        if b[j] in d:
            s=b[j]
            gf+=1
    if s==0:
        s='Volunteer cheated!'
    elif gf>1 :
            s='Bad magician!'
    print 'Case #%d: %s' %(i,s)
    k+=10
    s=0
    gf=0


