import string

f1 = open("A-large.in","r")
f2 = open("out.txt","w")

data = f1.readlines()
k = int((data[0].split())[0])
ind=1
for i in range(k):
    dim=data[ind].split()
    ind+=1
    r=int(dim[0])
    c=int(dim[1])
    A=[None]*r
    for j in range(r):
        B={}
        line=data[ind].split()
        ln=line[0]
        for k in range(c):
            if ln[k]!="?":
                B[k]=ln[k]
        ind+=1
        A[j]=B
    C=[None]*r
    rmin=-1
    for j in range(r):
        if (len(A[j])>0):
            B=A[j].keys()
            B=[int(x) for x in B]
            B.sort()
            l=len(B)
            strn=""
            if l>=2:
                strn+=A[j][B[0]]*B[1]
                if l!=2:
                    for k in range(1,l-1):
                        strn+=A[j][B[k]]*(B[k+1]-B[k])
                strn+=A[j][B[l-1]]*(c-B[l-1])
            if l==1:
                strn+=A[j][B[0]]*c
            C[j]=strn
            if rmin==-1:
                rmin=j
            rmax=j
        elif rmin==-1:
            C[j]=None
        else:
            C[j]=C[rmax]
    for j in range(rmin):
        C[j]=C[rmin]
    f2.write("Case #"+str(i+1)+":\n")
    for j in range(r):
        f2.write(C[j]+"\n")
    
f1.close()
f2.close()
