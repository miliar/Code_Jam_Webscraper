from operator import itemgetter
import math
from collections import OrderedDict

t = int(raw_input())  # read a line with a single integer

def solve(array):
    array = sorted(array, key=lambda x: x[0])[::-1]
    rh_d = {}
    for i in xrange(len(array)):
        rh_d[i] = array[i][0]*array[i][1]
    rh_d = OrderedDict(sorted(rh_d.items(), key=lambda x: x[1])[::-1])

    res = 0
    for i in xrange(n-k+1):
        tmp = math.pi*array[i][0]*array[i][0]
        tmp += 2*math.pi*array[i][0]*array[i][1]
        del rh_d[i]
        count = 0
        for j in rh_d:
            if count == k-1:
                break
            tmp += 2*math.pi*rh_d[j]
            count += 1
        if tmp > res:
            res = tmp
    return res

for i in xrange(1, t + 1):
  n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  array = []
  for j in xrange(n):
      array.append([int(s) for s in raw_input().split(" ")])
  res = solve(array)
  print "Case #{}: {}".format(i, res)
  # check out .format's specification for more formatting options
