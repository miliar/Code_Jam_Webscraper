from sys import *
from copy import copy

def mul(seq):
  return reduce(lambda x, y: x * y, seq, 1)
  
def solve(case, A, B, Ps):
  L = B-A
  mulPs = mul(Ps)
  
  # keep typing
  expected = (L+1) * mulPs + (L+B+2) * (1 - mulPs)
  
  # backspace 1 - A-1
  for stroke in xrange(1, A):
    _mulPs = mulPs
    _expected = (L+stroke*2+1)
    for _stroke in xrange(1, stroke+1):
      _Ps    = copy(Ps)
      _Ps[-_stroke] = 1 - Ps[-_stroke]
      _mulPs += mul(_Ps)
    expected = min(expected, _expected * _mulPs + (L+stroke*2+2+B) * (1 - _mulPs))
  
  # backspace all
  expected = min(A*2+L+1, expected)
  
  # right away
  expected = min(expected, B+2)
  print "Case #%d: %.6f" % (case, expected)

T = int(raw_input())
for case in xrange(1, T+1):
  l = map(int, stdin.readline().split())
  A = l[0]
  B = l[1]
  Ps = map(float, stdin.readline().split())
  solve(case, A, B, Ps)