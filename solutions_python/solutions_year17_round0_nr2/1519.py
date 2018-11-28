def LargestTidyNum(n):
    x=[int(i) for i in str(n)]
    lenx=len(x)
    l=lenx-1
    while(l>0):
        if(x[l]==0):
            i=0
            for j in range(l+1,lenx):
                x[j]=9
            while(x[l-i]==0):
                x[l-i]=9
                i+=1
            x[l-i]-=1
        elif(x[l]<x[l-1]):
            while(l<=lenx-1):
                x[l]=0
                l+=1
            l=lenx-1
        else:
            l-=1
    s = reduce(lambda x,y: x+str(y), x, '')
    return int(s)
t = int(raw_input())
for i in xrange(1, t + 1):
  n= int(raw_input())
  print "Case #{}: {}".format(i, LargestTidyNum(n));