def countFlip(s, k):
  s = list(s)
  i = 0
  flip = 0
  while i < len(s):
    if s[i] == '-':
      flip += 1
      if i + k > len(s):
        return -1
      for _ in xrange(k):
        if s[i + _] == '-':
          s[i + _] = '+'
        else:
          s[i + _] = '-'
    i += 1
  return flip


T = input()
for t in xrange(T):
  s, k = raw_input().split(" ")
  k = int(k)
  r = countFlip(s, k)
  print "Case #" + str(t + 1) + ":",
  if r >= 0:
    print str(r)
  else:
    print "IMPOSSIBLE"