import sys
f=open(sys.argv[1])
T=int(f.readline())
case=1
while case<T+1:
    a1=int(f.readline())-1
    arr1=[]
    for i in range(0,4):
        line=f.readline().split()
        if i!=a1: continue
        for n in line:
            arr1.append(int(n))

    #print arr1

    a2=int(f.readline())-1
    arr2=[]
    for i in range(0,4):
        line=f.readline().split()
        if i!=a2: continue
        acnt=0
        ans=0
        for n in line:
            if int(n) in arr1:
                ans=int(n)
                acnt+=1

        if acnt==0:
            print "Case #%d: Volunteer cheated!"%(case,)
        elif acnt==1:
            print "Case #%d: %d"%(case,ans)
        elif acnt>1:
            print "Case #%d: Bad magician!"%(case,)


    case+=1
