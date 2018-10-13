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
    items = line.split()
    a = int(items[0])
    b = int(items[1])
    ret = 0
    for x in range(a, b + 1):
      st = str(x)
      n = len(st)
      ss = set([st])
      for i in range(1, n):
        s = st[i:n] + st[0:i]
        #print st, s
        if s[0] == '0' or s in ss:
          continue
        y = int(s)
        if a <= y and y <= b:
          ret = ret + 1
          ss.add(s)
    print 'Case #{0}: '.format(str(idx)) + str(ret / 2)

if __name__ == "__main__":
    main(sys.argv[1:])
