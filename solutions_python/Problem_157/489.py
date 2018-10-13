#!/bin/env python

def prod(a, b):
  if abs(a) == 1 or abs(b) == 1:
    return a * b
  if abs(a) == abs(b):
    return -1 if a == b else 1
  ret = 2+3+4 - abs(a) - abs(b)
  sign = [0,1,-1][(abs(b) - abs(a)) % 3]
  if a*b  < 0:
    sign *= -1
  return ret * sign

#def pp(a):
#  pos = ['0','1','i','j','k']
#  return pos[a] if a > 0 else '-' + pos[-a]
#
#for i in [1,2,3,4,-1,-2,-3,-4]:
#  for j in [1,2,3,4,-1,-2,-3,-4]:
#    print pp(i), pp(j), pp(prod(i, j))
#exit()

cases = int(raw_input())

def case():
  L, X = map(int, raw_input().split())
  chars = map(lambda c: 1 if c == '1' else ord(c) - ord('i') + 2, raw_input())
  if L != len(chars):
    raise Exception('Unexpected length')
  char_total = reduce(prod, chars)
  char_total = reduce(prod, [char_total] * (X % 4 + 4))
  if char_total != -1:
    return False

  running = 1
  saw_i = False
  for i in xrange(len(chars) * min(15, X)):
    running = prod(running, chars[i % len(chars)])
    if running == 2:
      saw_i = True
    if running == 4 and saw_i:
      return True
  return False
  

for i in xrange(cases):
  print 'Case #{}: {}'.format(i+1, 'YES' if case() else 'NO')
