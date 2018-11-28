import sys

def ceil_log(ell, p, c):
  """
   ceil(log_c(p / ell)), but I'm tired and don't want to have to
   worry about rounding errors, so I'm avoiding floating point arithmetic

   based on c >= 2 and p / ell <= 10**9, this takes at most ~30 iterations
  """
  i = 0
  while ell < p:
     i += 1
     ell *= c
  return i

if __name__ == '__main__':
  t = int(sys.stdin.next())
  for i, line in enumerate(sys.stdin):
    t -= 1
    ell, p, c = map(int, line.split())
    print "Case #{0}: {1}".format(i+1, ceil_log(1, ceil_log(ell, p, c), 2))
  assert t == 0


