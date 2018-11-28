def findLR(n, k):
  if n==0 or n==1:
    return (0,0)
  mid = n/2
  l=mid
  r=n-mid
  if l<r:
    s=mid+1
  else:
    s=mid
  l=s-1
  r=n-s
  if k==1:
    return (max(l,r), min(l,r))
  k=k-1
  if k%2!=0:
    k=k/2+1
    n=max(l,r)
  else:
    k=k/2
    n=min(l,r)
  return findLR(n,k)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  (mx, mn) = findLR(n,k)
  print "Case #{}: {} {}".format(i, mx, mn)


