#!/usr/bin/python
# coding: utf-8

t=int(raw_input())
for i in xrange(t):
    (n,k)=map(int,raw_input().split(' '))
    arr=[0] * (n+2)
    arr[0]=1
    arr[n+1]=1
    ans1=ans2=-1
    for j in xrange(k):
        min=[0] * (n+2)
        max=[0] * (n+2)
        for s in xrange(1,n+1):
            if(arr[s]==0):
                lcnt=rcnt=0
                for l in xrange(s,0,-1):
                    if(arr[l]==1):
                        break
                    lcnt+=1
                for r in xrange(s,n+1):
                    if(arr[r]==1):
                        break
                    rcnt+=1
                if(lcnt<rcnt):
                    min[s]=lcnt
                    max[s]=rcnt
                else:
                    min[s]=rcnt
                    max[s]=lcnt
        maxm=-1
        tmpind=-1
        ind=[0] * (n+2)
        cnt=0
        for s in xrange(1,n+1):
            if(min[s]>maxm):
                maxm=min[s]
                for x in xrange(0,n+2):
                    ind[x]=0
                ind[s]=1
                tmpind=s
                cnt=0
            elif(min[s]==maxm):
                cnt=1
                ind[s]=1
        if(cnt==0):
            arr[tmpind]=1
        else:
            maxm=-1
            tmpind=-1
            ind2=[0] * (n+2)
            cnt=0
            for s in xrange(1,n+1):
                if(ind[s]==1):
                    if(max[s]>maxm):
                        maxm=max[s]
                        for x in xrange(0,n+2):
                            ind2[x]=0
                        ind2[s]=1
                        tmpind=s
                        cnt=0
                    elif(max[s]==maxm):
                        cnt=1
                        ind2[s]=1
            if(cnt==0):
                arr[tmpind]=1
            else:
                for s in xrange(1,n+1):
                    if(ind2[s]==1):
                        arr[tmpind]=1
                        break
        ans1=max[tmpind]
        ans2=min[tmpind]
    print "Case #"+str(i+1)+": "+str(ans1-1)+" "+str(ans2-1)


