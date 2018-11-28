def is_plus(i):
  if i == '+':
    return True
  return False

for cas in xrange(1,1+input()):
  print "Case #%s:" % cas,
  s,k = raw_input().split()
  s = map(is_plus,s)
  k = int(k)
  count = 0

  for c in range(0,len(s)-k):
    if not s[c]:
      count += 1
      for i in range(c,c+k):
        s[i] = not s[i]


  for c in range(len(s)-k,len(s)):
    if not s[c]:
      count += 1
      for i in range(len(s)-k,len(s)):
        s[i] = not s[i]
      break

  if all(s):
    print count
  else:
    print "IMPOSSIBLE"
