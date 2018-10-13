# by dave.t

import math

def foo(n):
  tot = 0
  if n == 0:
    return 0
  for i in range(1, n + 1):
    tot += i
  return tot


with open('input.txt') as fin:
  with open('output.txt', mode='w') as fout:
    T = int(fin.readline())
    for t in range(1, T + 1):
      vals = [int(x) for x in fin.readline().split()]
      assert(len(vals) == 3)
      R = vals[0]
      C = vals[1]
      W = vals[2]

      total = int(math.floor(C / W)) * R + (W - 1)
      if C % W > 0:
        total += 1



      print("{}".format(total))
      fout.write("Case #{}: {}\n".format(t, total))

