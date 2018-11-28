def solve(S):

  N = map(int,list(S))

  friends,standing = 0,0

  for i in xrange(1, len(N)):
    standing += N[i-1]
    if N[i] > 0:
      friends += max(0,i - standing - friends)

  return friends

if __name__ == '__main__':

  T = int(raw_input().strip())
  for t in xrange(T):
    S = raw_input().strip().split()[1]
    print "Case #%d: %d" % (t+1, solve(S))


