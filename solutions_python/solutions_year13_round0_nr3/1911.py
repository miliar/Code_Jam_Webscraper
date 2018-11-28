import math
f=open("C-small-attempt1.in","r")
w=open("sol.txt","w")
n=f.readline()
n=int(n)+1
x=1
palin=[]
roots=[]

while x<n:
    palin=[]
    roots=[]
    intv=f.readline()
    ilist=intv.split()
    print ilist
    a=int(ilist[0])
    b=long(ilist[1])+1
    a=range(a,b)
    for i in a:
        ab=list(str(i))
        bb=list(str(i))
        bb.reverse()
        if ab==bb:
            palin.append(i)
    for i in palin:
        a=math.sqrt(i)
        roots.append(a)
    palin=[]
    for p in range(0,len(roots)):
        if roots[p]%1==0.0:
            roots[p]=int(roots[p])
        else:
            roots[p]="xy"
    for i in roots:
        ac=list(str(i))
        bc=list(str(i))
        bc.reverse()
        if ac==bc:
            palin.append(i)
    w.write("Case #%d: %d\n" %(x,len(palin)))
    x=x+1
f.close()
w.close()


