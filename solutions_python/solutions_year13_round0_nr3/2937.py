#! /usr/bin/env python
import sys
import math

def is_fair(num):
  num = str(num)
  return num == num[::-1]
  
def is_square(num):
  root = math.sqrt(num)
  if int(root + 0.5) ** 2 == num:
    if is_fair(int(root)):
      return True
    return False
  else:
    return False
  
if __name__ == '__main__':
  f = file(sys.argv[1])
  T = int(f.readline())
  for i in xrange(T):
    A, B = f.readline().rstrip('\n').split(' ')
    count = 0
    for num in xrange(int(A), int(B) + 1):
      if is_fair(num) and is_square(num):
        count += 1
    print 'Case #{}: {}'.format(i+1, count)