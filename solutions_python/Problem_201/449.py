import heapq
T = int(raw_input())
for q in xrange(1, T+1):
  N,K = map(int, raw_input().split())
  a = {N: 1}
  while True:
    k = sorted(a.keys(), reverse=True)[0]
    if K <= a[k]:
      if k % 2 == 0:
        print "Case #" + str(q) + ": " + str(k/2) + " " + str(k/2-1)
      else:
        print "Case #" + str(q) + ": " + str((k-1)/2) + " " + str((k-1)/2)
      break
    if k % 2 == 0:
      k1 = k/2
      k2 = k1 - 1
      if k1 not in a:
        a[k1] = 0
      if k2 not in a:
        a[k2] = 0
      a[k1] += a[k]
      a[k2] += a[k]
    else:
      k1 = (k - 1) / 2
      if k1 not in a:
        a[k1] = 0
      a[k1] += a[k] * 2
    K -= a[k]
    del a[k]
