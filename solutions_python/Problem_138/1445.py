import sys

def play_normal(N, K):
  N.sort()
  K.sort()
  score = 0
  
  for n in N:
    ks = [k for k in K if k > n]

    if not ks:
      score += 1
    else:
      K.remove(ks[0])

  return score

def play_deceit(N, K):
  N.sort()
  K.sort()
  score = 0

  while len(N) > 0 and len(K) > 0:
    n = N[0]
    k = K[0]

    if (n > k):
      score += 1
      N.remove(n)
      K.remove(k)
    else:
      N.remove(n)

  return score

tests = int(sys.stdin.readline())

for i in range(0, tests):
  blocks = int(sys.stdin.readline())
  line = sys.stdin.readline()
  N = [float(n) for n in line.split()]
  line = sys.stdin.readline()
  K = [float(n) for n in line.split()]

  deceit = play_deceit(list(N), list(K))
  normal = play_normal(list(N), list(K))

  print "Case #%d: %d %d" % ((i + 1), deceit, normal)
