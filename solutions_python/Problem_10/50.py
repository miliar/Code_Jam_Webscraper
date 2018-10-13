import sys, math

inputcases = int(sys.stdin.readline())
for caseno in range(inputcases):
  print 'Case #%d:' % (caseno+1),
  
  (p, k, l) = map(int, sys.stdin.readline().split())
  freqs = map(int, sys.stdin.readline().split())

  freqs.sort()
  freqs.reverse()

  total = 0
  for i in range(len(freqs)):
    total += freqs[i] * (i / k + 1)

  print total
