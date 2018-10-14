def cov(lm1,n,m):
    i=0
    co=[]
    while i<m:
        j=0
        cm=[]
        while j<n:
            cm.append(lm1[j][i])
            j=j+1
        cm=''.join(cm)
        i=i+1
        co.append(cm)

    return co

def maxm(lm1):
    l=len(lm1)
    i=0
    m=int(lm1[0])
    while i<l:
        if m<int(lm1[i]):
            m=int(lm1[i])
        i=i+1
    return m

def checkmt(lm1,n,m):
    sm=[]
    i=0
    while i<n:
        sm.append([])
        j=0
        while j<m:
            sm[i].append(2)
            j=j+1
        i=i+1
    i=0
    while i<n:
        mp=maxm(lm1[i])
        j=0
        while j<m:
            if sm[i][j]>mp:
                sm[i][j]=mp
            j=j+1
        i=i+1
    i=0
    cv=cov(lm1,n,m)
    while i<m:
        mp=maxm(cv[i])
        k=0
        while k<n:
            if sm[k][i]>mp:
                sm[k][i]=mp
            k=k+1
        i=i+1
    i=0
    while i<n:
        j=0
        while j<m:
            if sm[i][j] != int(lm1[i][j]):
                return 0
            j=j+1
        i=i+1
    return 1
        
    
    
    
    
def lawnMower():
    infile=file("G:\ONLINE COURSES\Google Code Jam 2013\BSIN.IN",'r')
    whole=infile.readlines()
    infile.close()
    t=int(whole[0])
    output=[]
    i=0
    l=1
    while(i<t):
        nm=whole[l].split()
        n=int(nm[0])
        m=int(nm[1])
        lm=[]
        j=0
        while j<n:
            lm.append(whole[l+j+1])
            j=j+1
        lm1=[]
        j=0
        while j<n:
            lm1.append([])
            lm1[j]=''.join((lm[j][:-1]).split())
            j=j+1
        c=checkmt(lm1,n,m)
        output.append(c)
        l=l+n+1
        i=i+1

    i=0
    while i<t:
        if output[i]==1:
            print"Case #"+str(i+1)+": YES"
        elif output[i]==0:
            print"Case #"+str(i+1)+": NO"
        i=i+1
        
        
            
if __name__=="__main__":
    lawnMower()
