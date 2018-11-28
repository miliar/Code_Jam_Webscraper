f=open("C:\Users\Bea\Documents\GCJ\B-large.in.txt")
g=open("C:\Users\Bea\Documents\GCJ\B-large.out", "w")


c=int(f.readline())
for case in range(c):
    line=f.readline()
    l = [int(x) for x in line.split()]
    N=l[0]
    S=l[1]
    p=l[2]
    t=l[3:]
    for i in range (len(t)):
        if p>0:
            if p==1:
                if t[i]==0:
                    N=N-1
            elif t[i]<3*p-2:
                if t[i]>=3*p-4:
                    S=S-1
                else:
                    N=N-1
    if S<0:
        R=N+S
    else:
        R=N

    g.write("Case #"+str(case+1)+": "+str(R)+'\n')

f.close()
g.close()
