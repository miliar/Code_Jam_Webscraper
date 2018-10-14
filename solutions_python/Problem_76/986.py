import operator
import string
import sys

def psum(l):
  return reduce(operator.xor, l)

def c(j, n, ints):
  max = -1
  i = 1
  limit = 2**n - 1
  ints.sort(reverse = True)
  
  while i < limit:
    bin_i = string.zfill(bin(i)[2:], n)
    s = []
    p = []
    for k, b in enumerate(bin_i):
      if b == '0':
        s.append(ints[k])
      else:
        p.append(ints[k])
    sx = psum(s)
    px = psum(p)
    if (sx == px):
      ss = sum(s)
      if (ss > max):
        max = ss
        break
    i += 1
  
  if max > -1:
    print 'Case #%d: %d' % (j, max)
  else:
    print 'Case #%d: NO' % (j)
  
if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f:
    t = int(f.readline())
    for j in range(1, t + 1):
      n = int(f.readline())
      ints = [int(x) for x in f.readline().split()]
      c(j, n, ints)
