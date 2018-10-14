
from operator import xor

CASES = int(raw_input())

def to_bin(i, p):
  R = []
  while i:
    R.append(str(i%2))
    i /= 2
  R.reverse()

  return ''.join(R).rjust(p,'0')
    

def case():
  raw_input()
  N = [int(x) for x in raw_input().split()]
  B = max(x.bit_length() for x in N)
  NB = [to_bin(x,B) for x in N]

  if reduce(xor, N) != 0:
    return 'NO'

  return sum(N) - min(N)

for C in range(CASES):
  ret = case()
  print 'Case #%d: %s' % (C+1, ret)
    

