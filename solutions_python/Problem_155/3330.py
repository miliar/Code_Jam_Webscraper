T = int(raw_input())
for case in xrange(T):
  [S, s] = raw_input().split()
  ct = 0
  add = 0
  for i in xrange(len(s)):
    qt = ord(s[i]) - ord('0')
    if ct < i:
      add += i - ct
      ct += i - ct
    ct += qt

  print("Case #%d: %d" % (case+1,add))




