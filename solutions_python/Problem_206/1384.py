andmed=open("steed.in","r")
t=int(andmed.readline())
vastused=list()
for i in range(t):
    xd=andmed.readline().strip().split()
    d=float(xd[0])
    n=int(xd[1])
    for j in range(n):
        xdt=andmed.readline().strip().split()
        k=float(xdt[0])
        s=float(xdt[1])
        tn=(d-k)/s
        if j==0:
            tr=tn
        if tn>tr:
            tr=tn
    kiirus=d/tr
    vastus="Case #"+str(i+1)+": "+str(kiirus)+"\n"
    vastused.append(vastus)
andmed.close()

goo=open("steed.out","w")
for i in range(t):
    goo.write(vastused[i])
goo.close()
