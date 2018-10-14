def spacel(lst,i):

    for j in range(i-1,-1,-1):

        if(lst[j]==1):

            return (i-j-1)

def spacer(lst,i):

    for j in range(i+1,len(lst)+1):

        if(lst[j]==1):

            return (j-i-1)

t=int(input())

for T in range(1,t+1):

    n,k=map(int,(input().split()))

    lst=[1]

    minm=[-1 for i in range(n+2)]

    maxm=[-1 for i in range(n+2)]

    for i in range(n):

        lst.append(0)

    lst.append(1)

    #print(n,k)

    #print(lst)

    for cnt in range(k):

        l2=[]

        for i in range(1,len(lst)):

            if(lst[i]==0):

                left=spacel(lst,i)

                right=spacer(lst,i)

                minm[i]=min(left,right)

                maxm[i]=max(left,right)

        #print(minm)

        #print(maxm)

        a = max(minm)

        indices = [p for p, v in enumerate(minm) if v == a]

        #print(indices)

        if(len(indices)==1):

            lst[indices[0]]=1

            minm[indices[0]]=-1

            maxm[indices[0]]=-1

            #print(lst)

            #print(indices[0])

            if(cnt==k-1):

                lft=spacel(lst,indices[0])

                rgt=spacer(lst,indices[0])

                #print(lft,rgt)

        else:

            for z in indices:

                l2.append(maxm[z])

            b = max(l2)

            indices1 = [p for p, v in enumerate(maxm) if v == b]

            #print(indices1)

            lst[indices1[0]]=1

            minm[indices1[0]]=-1

            maxm[indices1[0]]=-1

            #print(lst)

            #print(indices1[0])

            if(cnt==k-1):

                lft=spacel(lst,indices1[0])

                rgt=spacer(lst,indices1[0])

                #print(lft,rgt)

    print("Case #"+str(T)+": "+str(max(lft,rgt))+" "+str(min(lft,rgt)))
            
        