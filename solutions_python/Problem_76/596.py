#!/usr/bin/python

fname = 'C-large'

def solve(N, s):
  N = int(N)
  s = s.split(' ')
  total = 0
  minimum = int(s[0])
  xor = 0
  for i in xrange(N):
    C = int(s[i])
    total += C
    xor ^= C
    if C < minimum: minimum = C
  if xor != 0: return 'NO'
  return total-minimum

fin = file(fname+'.in')
T = int(fin.readline().strip())
fout = file(fname+'.out', 'w')
for i in xrange(T):
  fout.write('Case #%s: %s\n' %(i+1, solve(fin.readline(), fin.readline())))

