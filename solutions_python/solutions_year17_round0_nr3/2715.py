def ls(n):
    if n%2==1:
        return (n-1)/2
    else:
        return (n-2)/2
def rs(n):
    return (n-1-ls(n))
def which_stall(N,K):
    l=[N]
    for i in range (0,K-1):
        r=l.index(max(l))
        z=l[r]
        l[r]=ls(z)
        l.insert(r+1,rs(z))
    r=l.index(max(l))
    return (max(ls(l[r]),rs(l[r])),min(ls(l[r]),rs(l[r])))
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]
  t=which_stall(n,k)
  print "Case #{}: {} {}".format(i,t[0],t[1])
