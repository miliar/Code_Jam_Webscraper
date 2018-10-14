# cook your dish here
def heapify(n,p):
        l=[n+1,n]
        i,count=(1,0)
        if(n==p):
                return 0,0
        m=n
        while(i<=n+1):
                if m==0:
                        l=l+[0,0]
                else:
                        if(m%2==0):
                                l=l+[int((m)/2),int((m-2)/2)]
                        if(m%2==1):
                                l=l+[int((m-1)/2),int((m-1)/2)]
                if(i==p):
                        return l[2*i],l[2*i+1]
                l=sorted(l,reverse=True)
                i=i+1
                m=l[i]
t=int(input())
for i in range(1,t+1):
        n,k = [int(s) for s in input().split(" ")]
        ls,rs=heapify(n,k)
        print("Case #{}: {} {}".format(i,ls,rs))
