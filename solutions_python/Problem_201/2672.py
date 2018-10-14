t = int(raw_input())
for i in xrange(1, t+1):
  n,m=[int(s) for s in raw_input().split(" ")]
  k=1
  l = []
  l.append(n)
  stamp = 0
  while k <= m:
    stamp = l.pop(0)
    if stamp==0:
        ls = 0
        rs = 0
        break
    if stamp%2==1:
        ls = stamp//2
        rs = stamp//2
        l.append(ls)
        l.append(rs)
    else:
        ls = stamp//2-1
        rs = stamp//2
        l.append(rs)
        l.append(ls)
    l.sort(reverse = True)
    k+=1
  print "Case #{}: {} {}".format(i, max(ls,rs),min(ls,rs))