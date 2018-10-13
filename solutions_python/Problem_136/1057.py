import sys

def solution(f):
  C,F,X = map(float, f.readline().split())
  rate = 2
  t = X/rate
  ct = 0
  while t > (X / (rate + F) + C / rate + ct):
    ct += C / rate
    t = X / (rate + F) + ct
    rate = rate + F
  return t

f = sys.stdin
T = int(f.readline())
for x in range(T):
  print "Case #{}: {}".format((x + 1),solution(f))
