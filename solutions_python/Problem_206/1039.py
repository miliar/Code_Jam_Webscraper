def Cruise(D,N):
    max1=0
    for i in range(1,N+1):
        K,S= [float(j) for j in raw_input().split(" ")]
        temp=(D-K)/S
        if(temp>max1):
            max1=temp
    return (D/max1)

t = int(raw_input())
for i in xrange(1, t + 1):
  D,N= [int(j) for j in raw_input().split(" ")]
  result=Cruise(D,N)
  print "Case #{}: {}".format(i,result);