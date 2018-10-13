def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

for case in xrange(1, int(raw_input())+1):
  line = map(int, raw_input().split())
  N, T = line[0], line[1:]
  delta = [abs(T[i]-T[0]) for i in xrange(1, N)]
  factor = delta[0]
  for i in xrange(1, len(delta)):
    factor = gcd(factor, delta[i])
  answer = factor - (T[i] % factor)
  if answer == factor:
    answer = 0
  print "Case #%d: %d" % (case, answer)
