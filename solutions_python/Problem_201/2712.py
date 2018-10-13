def check(s,li=0,pi=0,co=1):
    hi=[]
    if co==0:
        l1=[]
        l2=[]
        for i in range(len(s)):
            l1.append(min(s[i][0],s[i][1]))
            l2.append(max(s[i][0],s[i][1]))
        li=max(l1)
        pi=max(l2)
        co+=1
    while True:    
       if ((li,pi)in s):
          return (li,pi)
       elif ((pi,li)in s):
          return(pi,li)
       else:
          if pi>0:
             pi-=1
             return(check(s,li,pi))
          elif li>0:
             li-=1
             return(check(s,li,pi))
def  bfill(s,inde,b):
    global jim,k,iim,out
    cop=0
    (li,pi)=check(s=s,co=cop)
    for i in range(len(s)):
        if (li==s[i][0] and pi==s[i][1]) or (pi==s[i][0] and li==s[i][1]):
            j=inde[i]
            break
    b[j]='0'
    if jim==k[iim]-1:
        out.append((pi,li))
    return b
def ebl(v,b):
    c=0
    for i in range(v,0,-1):
        if b[i]!='0':
            c+=1
        else:
            break
    return c-1
def ebr(v,b):
    c=0
    for i in range(v,len(b)):
        if b[i]!='0':
            c+=1
        else:
            break
    return c-1
def scre(b):
    s=[]
    inde=[]
    for i in range(0,len(b)):
        if b[i]=='.':
            s.append((ebl(i,b),ebr(i,b)))
            inde.append(i)
    return s,inde        
def bcreate(n):
    c=[]
    for i in range(0,n+2):
        if i==0 or i==n+1:
            c.append('0')
        else:
            c.append('.')
    return c
n=int(input())
inp=[]
k=[]
b=[]
out=[]
for i in range(0,n):
    s=input().strip().split(' ')
    inp.append(int(s[0]))
    k.append(int(s[1]))
for i in range(0,n):
   b.append(bcreate(inp[i]))
for iim in range(0,n):
    for jim in range(0,k[iim]):
        (iset,ipop)=scre(b[iim])
        b[iim]=(bfill(iset,ipop,b[iim]))
for i in range(len(out)):
    print('case #',i+1,': ',out[i][0],' ',out[i][1],sep='')
