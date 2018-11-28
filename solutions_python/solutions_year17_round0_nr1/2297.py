def flip(S,K,i):
    for p in range(i, i+K):
        if S[p] == '-': S[p:p+1] = '+'
        else: S[p:p+1] = '-'
    return S

def solve(S, K):
    # Go through S and then flip k starting with the first - from the left
    # print S
    ans = 0
    for i in range(0, len(S)-K+1):
        # print i
        if S[i] == '-':
            S = flip(S, K, i)
            ans += 1
            # print S

    # If the last K are still unflipped, we're doomed
    # print "Final S:"
    # print "".join(S)
    if "".join(S[len(S)-K:]) != '+'*K:
        ans = "IMPOSSIBLE"

    return ans

T = int(raw_input())  # read a line with a single integer
for tt in xrange(1, T + 1):
  data = raw_input().split(" ")
  S = list(data[0])
  K = int(data[1])

  ans = solve(S, K)

  print "Case #{}: {}".format(tt, ans)