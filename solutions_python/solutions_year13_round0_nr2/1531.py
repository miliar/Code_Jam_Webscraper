f=open("biner.in","r")
w=open("sol.in","w")
n=f.readline()
n=int(n)+1
x=1
maxh="2"

while x<n:
    u=0
    lawn=[]
    mylawn=[]
    siz=f.readline()
    siz=siz.split()
    for i in range(0,int(siz[0])):
        h=f.readline()
        h=h.split()
        lawn.append(h)
    for i in range(0,int(siz[0])):
        mylawn.append([])
        for o in range(0,int(siz[1])):
            mylawn[i].append(maxh)
            
    for i in range(0,int(siz[0])):
        u=0
        for o in range(0,int(siz[1])):
            if lawn[i][o]=="2":
                u=u+1
                break
        if u==0:
            for o in range(0,int(siz[1])):
                mylawn[i][o]="1"
    if mylawn!=lawn:
        for i in range(0,int(siz[1])):
            u=0
            for o in range(0,int(siz[0])):
                if lawn[o][i]=="2":
                    u=u+1
                    break
            if u==0:
                for o in range(0,int(siz[0])):
                    mylawn[o][i]="1"
    if mylawn==lawn:
        w.write("Case #%d: YES\n" %(x))
    else:
        w.write("Case #%d: NO\n" %(x))
    x=x+1
w.close()
f.close()
