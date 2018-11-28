# def largestSegment(l):
#
#     x=[j-i-1 for i, j in zip(l[:-1], l[1:])]
#     y=x.index(max(x))
#     return l[y]+1,l[y+1]-1
def BS(N,K):
    # l=[0,N+1]
    # while(K>0):
    #     x,y=largestSegment(l)
    #     width=y-x+1;
    #     if((width)%2==1):
    #         element=x+(width/2)
    #     else:
    #         element=x+(width/2)-1
    #     i=0
    #     while(l[i]<element):
    #         i+=1
    #     l.insert(i,element)
    #     K-=1
    # return max(l[i]-l[i-1]-1,l[i+1]-l[i]-1),min(l[i]-l[i-1]-1,l[i+1]-l[i]-1)
    flag=0
    while(K>0):
        if(N%2==0):
            if(K%2==0):
                N=N/2
                K=K/2
            else:
                N=(N/2)-1
                K=(K-1)/2
                flag=1
        else:
            if(K%2==0):
                N=(N-1)/2
                K=K/2
            else:
                N=(N-1)/2
                K=(K-1)/2
                flag=0
    return N+flag,N

t = int(raw_input())
for i in xrange(1, t + 1):
  N,K= [int(j) for j in raw_input().split(" ")]
  Max,Min=BS(N,K)
  print "Case #{}: {} {}".format(i,Max,Min);