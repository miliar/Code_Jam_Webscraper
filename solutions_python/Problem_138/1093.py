import sys

def war(N, naomi, ken):
  naomi = naomi[:]
  ken = ken[:]
  for i in xrange(N):
    found = False
    for j in xrange(N-i):
      if ken[j]>naomi[0]:
        del ken[j]
        found = True
        break
    if found:
      del naomi[0]
    else:
      return N - i
  return 0

def deceit(N, naomi, ken):
  score = 0
  for i in xrange(N):
    if naomi[0]>ken[0]:
      score += 1
      del naomi[0]
      del ken[0]
    else:
      del naomi[0]
      del ken[-1]

  return score

def main():
  T = int(sys.stdin.readline())
  for i in xrange(T):
    global N, naomi, ken
    N = int(sys.stdin.readline())
    naomi = [float(x) for x in sys.stdin.readline().split()]
    ken = [float(x) for x in sys.stdin.readline().split()]
    naomi.sort()
    ken.sort()
    
    w = war(N, naomi, ken)
    d = deceit(N, naomi, ken)
    
    print "Case #%d: %d %d" % (i+1, d, w)

main()