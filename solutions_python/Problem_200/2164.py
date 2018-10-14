andmed=open("arvud.txt","r")
t=int(andmed.readline())
vastused=list()
def delet(n):
    if n[0]==0:
        del n[0]
        return delet(n)
def funk(n):
    delet(n)
    for j in range(1, len(n)):
        if n[j]<n[j-1]:
            n[j-1]=n[j-1]-1
            for k in range(j, len(n)):
                n[k]=9
            funk(n)
            break
                
for i in range(t):
    n=int(andmed.readline())
    n=str(n)
    n=list(n)
    for kappa in range(len(n)):
        n[kappa]=int(n[kappa])

    funk(n)

    for kappa in range(len(n)):
        n[kappa]=str(n[kappa])
        
    nst="".join(n)
    lisandub="Case #"+str(i+1)+": "+nst
    vastused.append(lisandub)
andmed.close()

xdd=open("aout.txt","w")
for lolz in vastused:
    xdd.write(lolz)
    xdd.write("\n")
xdd.close()
