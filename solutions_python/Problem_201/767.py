import os
import math

def solve(N, K):
  small = (N-1) / 2
  large = N / 2
  n_small = 1
  n_large = 1
  while True:
    if K <= (n_large + n_small) / 2:
      if n_large > n_small:
        if K <= (n_large - n_small) / 2:
          return (large, large)
        else:
          return (small, large)
      else:
        if K <= n_large:
          return (small, large)
        else:
          return (small, small)

    K -= (n_large + n_small) / 2
    if small % 2 == 1 and large % 2 == 1:
      n_small = n_small * 2
      n_large = n_large * 2
      small = small / 2
      large = large / 2
    elif small % 2 == 1 and large % 2 == 0:
      n_small = n_small * 2 + n_large
      n_large = n_large
      small = small / 2
      large = large / 2
    elif small % 2 == 0 and large % 2 == 1:
      n_small = n_small
      n_large = n_large * 2 + n_small
      small = (small - 1) / 2
      large = large / 2
    else:
      n_small = n_small * 2
      n_large = n_large * 2
      small = (small - 1) / 2
      large = large / 2


fin = open('C-large.in', 'r')
fout = open('C.out', 'w')
for i, line in enumerate(fin):
  if i == 0:
    t = int(line)
    continue
  line = line.strip()

  N, K = line.split()
  N = int(N)
  K = int(K)

  res = solve(N, K)

  res = "%s %s" % (res[1], res[0])

  out_str = 'Case #%d: %s\n' % (i, res)
  print out_str
  fout.write(out_str)
fin.close()
fout.close()
