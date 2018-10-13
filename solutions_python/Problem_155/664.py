def solve(S):
  psum = 0
  lack = 0
  for i in range(len(S)):
    Si = int(S[i])
    if psum < i:
      lack += i - psum
      psum = i
    psum += Si
  return lack


f = open('A-large.in', 'r')
T = int(f.readline())
for i in range(T):
  Smax, S = f.readline().split()
  print 'Case #%d: %d' % (i+1, solve(S))
