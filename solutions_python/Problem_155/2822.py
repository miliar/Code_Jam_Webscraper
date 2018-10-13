rIn = lambda: raw_input().strip()

T = int(rIn())
for t in xrange(T):
  S, P = map(str, rIn().split())
  S = int(S)
  ans, cur = 0, 0
  for shyness, num in enumerate(P):
    num = int(num)
    if num != 0 and cur < shyness:
      ans += (shyness-cur)
      cur += (shyness-cur)
    cur += num
  print 'Case #{}: {}'.format(t+1, ans)