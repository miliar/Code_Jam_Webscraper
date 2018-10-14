def maximize(ln,lk):
    ken=0
    naomi=0
    for i in range(1,N+1):
        if lk[0]>ln[-1]:
            del(ln[0])
            del(lk[-1])
            ken+=1
        else:
            for j in range(0,N-i+2):
                if ln[j]>lk[0]:break
            del(ln[j])
            del(lk[0])
            naomi+=1
    return naomi
def war(ln,lk):
    ken=0
    naomi=0
    for i in range(1,N+1):
       if ln[-1]>lk[-1]:
          del(lk[0])
          naomi+=1
       else:
          for j in range(0,N-i+2):
              if lk[j]>ln[-1]:break
          del(lk[j])
          ken+=1
       del(ln[-1])
    return naomi
T=int(input())
for i in range(1,T+1):
    N=int(input())
    tmp=input().split()
    map(int,tmp)
    ln=tmp
    tmp=input().split()
    map(int,tmp)
    lk=tmp
    ln.sort()
    lk.sort()
    (ln1,ln2,lk1,lk2)=(ln[:],ln[:],lk[:],lk[:])
    a=maximize(ln1,lk1)
    b=war(ln2,lk2)
    print("Case #",i,": ",a," ",b,sep="")
