def gen_conf(N):
  if N == 1:
    yield []
    return
  for conf in gen_conf(N-1):
    for c in [[], [N]]:
      yield conf + c

MOD = 100003

cache = {}
for N in xrange(2, 26):
  ans = 0
  for s in gen_conf(N-1):
    s += [N]
    rank = {}
    for i in xrange(len(s)):
      rank[s[i]] = i+1
    n = N
    while n in s and n != rank[n]:
      n = rank[n]
    if n == 1:
      ans += 1
      ans %= MOD
  cache[N] = ans

for case in xrange(1, int(raw_input())+1):
  N = int(raw_input())
  ans = cache[N]
  print "Case #%d: %d" % (case, ans)
