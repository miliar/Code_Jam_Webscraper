
INF = 1000000000

def flip(S, beg, end):
    ans = ''
    for i in xrange(len(S)):
        if beg <= i and i <= end:
            if S[i] == '-':
                ans += '+'
            else:
                ans += '-'
        else:
            ans += S[i]
    return ans

def solve(S, K):
    res = 0
    N = len(S)
    for i in xrange(N):
        if S[i] == '-':
            if i + K > N:
                return INF
            S = flip(S, i, i + K - 1)
            res += 1
    return res

T = int(raw_input().strip())
for _t in xrange(T):
  S, K = raw_input().strip().split(" ")
  K = int(K)

  ans = min(solve(S, K), solve(S[::-1], K))
  if ans >= INF:
      ans = "IMPOSSIBLE"

  print "Case #%d: %s" % (_t + 1, str(ans))
