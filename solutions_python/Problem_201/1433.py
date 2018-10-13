def Solve(n,m):
    if (n==m):
        return 0,0
    y=z=0
    a = {}
    a[n]=1
    for i in range(m):
        M = max(a)
        if M == 1:
            return 0,0
        if(M%2==1):
            y = z = M/2
            if a.has_key(y):
                a[y]+=2
            else:
                a[y]=2
            a[M]-=1
            if a[M]==0:
                del a[M]
        else:
            y = M/2
            z = y-1
            if a.has_key(y):
                a[y]+=1
            else:
                a[y]=1
            if a.has_key(z):
                a[z]+=1
            else:
                a[z]=1
            a[M]-=1
            if a[M]==0:
                del a[M]
    return y,z        
            

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, M = raw_input().split()  
  l,r = Solve(int(N),int(M))
  print "Case #{}: {} {}".format(i, l, r)

