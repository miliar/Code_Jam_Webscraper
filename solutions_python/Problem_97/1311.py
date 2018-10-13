


def rec(a, b):
  cnt = 0
  for start in range(a, b + 1):
    n = str(start)
    # 1 2 3
    was = {}
    for sp in range(1, len(n)):
      derr = n[sp:] + n[:sp]
      d = int(derr)
      if d > start and d <= b and (not d in was):
        cnt += 1
        was[d] = 1
  return cnt


n = int(raw_input())
for i in range(n):
  sa, sb = raw_input().split()
  print "Case #%d: %d" % (i + 1, rec(int(sa), int(sb)))
