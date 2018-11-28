from sys import stdin
read = stdin.readline

ints = lambda:map(int,read().split())
doubles = lambda:map(float,read().split())


def solve():
    A,B,K = ints()
    count = 0
    for a in range(A):
        for b in range(B):
            if a&b < K:
                count += 1
    return str(count)


for t in range(ints()[0]):
  ans = solve()
  print "Case #%d: %s" % (t+1,ans)