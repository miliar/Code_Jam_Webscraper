#
# Author: Cheng-Shih, Wong (code14)
# Email:  mob5566@gmail.com
#

from __future__ import print_function
import numpy as np

fre = open('in', 'rb')

'''
def raw_input():
  global fre 
  return fre.readline()
'''

t = int(raw_input())


for ti in xrange(1, t+1):
  s, k = raw_input().split()

  k = int(k)
  pan = []

  for c in s:
    if c=='+':
      pan.append(True)
    else:
      pan.append(False)

  pan = np.array(pan)
  cnt = 0

  for i in xrange(len(pan)-k+1):
    if not pan[i]:
      pan[i:i+k] = np.logical_xor(pan[i:i+k], True)
      cnt += 1

  ans = cnt if np.alltrue(pan) else 'IMPOSSIBLE'

  print("Case #{}: {}".format(ti, ans))

fre.close()
