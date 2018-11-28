t=int(input())
for case in range(t):
    n,k=map(int,input().split())
    stall=['']*n

    print('case #',end='')
    print((case+1),end='')

    if n==k:
        print(': 0 0')
        continue

    elif k==1:                #only one person goes
        if n%2==0 :          #even
            print(':',int(n/2),int(n/2-1))
        else:                #odd
            print(':',int(n/2),int(n/2))

        continue

    while k>0:
        #print(stall,k)
        #Calculate largest unfilled contiguous stall
        count=0
        low=0
        high=0
        minc=0
        maxc=0
        maxcount=0
        for i in range(n):
            if stall[i]=='0':
                high=i
                low=high+1
                count=0

            if stall[i]=='':
                high=i
                count+=1
                if count>maxcount:
                    minc=low
                    maxc=high
                    maxcount=count

        #print('bounds ',minc,maxc,stall)
        if maxcount%2==0:       #even
            point=int((maxc-minc)/2)+minc
            stall[point]='0'
            lc=point-minc
            rc=maxc-point

            #print('even',point,lc,rc)

            if k==1:
                print(':',max(rc,lc),min(rc,lc))
                break

        else:
            point=int((maxc-minc)/2)+minc
            stall[point]='0'
            lc=point-minc
            rc=maxc-point

            #print('odd',point,lc,rc)

            if k==1:
                print(':',max(rc,lc),min(rc,lc))
                break

        k-=1

    #print(stall)