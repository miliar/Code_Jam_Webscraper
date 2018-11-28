def call():
    ar1=[]
    ar2=[]
    a=int(input())
    for i in range(4):
        ar1.append(map(int,raw_input().split()))
    b=int(input())
    for i in range(4):
        ar2.append(map(int,raw_input().split()))
    cnt=0
    a-=1
    b-=1
    val=-1
    for i in range(4):
        for j in range(4):
            #print i,j
            if ar1[a][i]==ar2[b][j]:
                cnt+=1
                val=ar1[a][i]
    return (cnt,val)
t=int(input())
for t1 in range(1,t+1):
    (cnt,val)=call()
    print "Case #%d:"%(t1),
    if cnt==0: print "Volunteer cheated!"
    elif cnt>1:print "Bad magician!"
    else: print val
    
