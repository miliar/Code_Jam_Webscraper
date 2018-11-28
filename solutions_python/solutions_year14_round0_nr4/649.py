source="C:\Users\Mani\Desktop\cj\D-large.in"
dest="C:\Users\Mani\Desktop\cj\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=int(fin.readline())

for i in range(t):
    
    p=int(fin.readline())
    p=p-1
    q=p
    qq=q
    pp=p
    naomi=fin.readline()
    naomi=naomi.split(" ")
    naomi=map(float,naomi)
    naomi.sort()
    nm=[]
    for e in naomi:
        nm.append(e)
    ken=fin.readline()
    ken=ken.split(" ")
    ken=map(float,ken)
    ken.sort()
    kn=[]
    for e in ken:
        kn.append(e)
    w=0
    dw=0
    for j in range(pp+1):
       
        if naomi[0]>ken[p]:
            
            naomi.pop(0)
            ken.pop(0)
            p=p-1
            w=w+1
            
        else:
            b=[k for k in ken if k>naomi[0]]
            naomi.pop(0)
            ken.remove(b[0])
            p=p-1


    for j in range(pp+1):
       
        if nm[q]>kn[q]:
            
            nm.pop(q)
            kn.pop(q)
            q=q-1
            dw=dw+1
            
        else:
            
                      
            if len(nm)>1:
                nm.pop(0)
                kn.pop(q)
            else:
                nm.pop(q)
                kn.pop(q)
            q=q-1
            
    fout.write("Case #"+str(i+1)+": "+str(dw)+" "+str(w)+"\n")

fin.close()
fout.close()
        
