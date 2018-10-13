def f(n):
  s = `n`
  res = 0
  for i in xrange(len(s)):
    res = res * 10 + (ord(s[i])-ord('0'))
    if i+1 < len(s) and s[i] > s[i+1]:
      res -= 1
      right = 0
      for j in xrange(i+1, len(s)):
        right = right * 10 + 9
        res *= 10
      return f(res+right)
  return res

t = int(raw_input())
for tt in xrange(1, t+1):
  n = int(raw_input())
  print "Case #%d: %d" % (tt, f(n))
