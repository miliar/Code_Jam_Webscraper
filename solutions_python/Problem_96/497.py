#! python

import sys

def main(args):
  fin = open('input.txt', 'r')
  data = fin.read().split('\n')
  fin.close()
  nd = int(data[0])
  data = data[1:]
  idx = 0
  for line in data:
    idx = idx + 1
    if (idx > nd):
      break
    ret = 0
    nondet = 0
    items = line.split()
    n = int(items[0])
    s = int(items[1])
    p = int(items[2])
    items = items[3:]
    assert len(items) == n
    for item in items:
      x = int(item)
      si = (x + 2) / 3
      so = (x + 4) / 3
      if si >= p:
        ret = ret + 1
      else:
        if so == p and si == p - 1:
          nondet = nondet + 1
    if nondet > s:
      nondet = s
    if p == 1:
      nondet = 0
    print 'Case #{0}: '.format(str(idx)) + str(ret + nondet)

if __name__ == "__main__":
    main(sys.argv[1:])
