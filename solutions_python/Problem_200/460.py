T = int(raw_input())
for q in xrange(1, T+1):
  N = raw_input()
  a = []
  for i in xrange(len(N)):
    a.append(int(N[i]))
  for i in xrange(1, len(N)):
    if a[i-1] > a[i]:
      for j in xrange(i, len(N)):
        a[j] = 9
      a[i-1] -= 1
      for j in reversed(xrange(1, i)):
        if a[j-1] <= a[j]: break
        a[j] = 9
        a[j-1] -= 1
      break
  ans = 0
  for i in xrange(len(N)):
    ans = ans * 10 + int(a[i])
  print "Case #" + str(q) + ": " + str(ans)
