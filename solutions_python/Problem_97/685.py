import sys

T = int(sys.stdin.readline())

for t in range(1, T+1):
  a, b = map(int, sys.stdin.readline().strip().split())
  sa, sb = str(a), str(b)

  cnt = 0
  for i in range(a, b+1):
    s = str(i)
    used = set()
    if s[0] != '0':
      for j in range(1, len(s)):
        r = s[j:] + s[:j]
        if r[0] != '0' and sa <= r and r <= sb and s < r:
          if r not in used:
            used.add(r)
            cnt += 1
  print 'Case #%d: %d' % (t, cnt)
