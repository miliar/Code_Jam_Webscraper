import sys
from math import sqrt

def is_pal(n):
  l = list(str(n))
  l_rev = list(reversed(l))
  return l == l_rev 

# The code below has been used to generate all the palindroms below 10**100
# in ~ 5mins. The file is ~50MB so cannot embed it in the code.
# all_pals = [(0, 0), (1, 1), (1, 2), (1, 3)]
# 
# for digits in xrange(2, 101):
#   ten = 10**(digits-1)
#   for k in [1, 2]:
#     for pal_d, pal in all_pals:
#       if pal != 0 and pal_d & 1 != digits & 1: continue
#       if digits - 2 < pal_d: continue
#       to_add = (digits - pal_d) / 2
#       padded_pal = pal * 10**to_add
#       d = k + padded_pal + ten*k
#       if is_pal(d) and is_pal(d*d):
#         all_pals.append((digits, d))
# 
# for _, d in all_pals:
#   print d
def sqr(x): return x * x
pal_file = open('pals.txt', 'r')
pals = pal_file.readlines()
pals = map(lambda x: sqr(int(x)), pals)
pal_file.close()

def f(lower_bound, upper_bound):
  lo, up = 0, len(pals) - 1
  while up - lo > 1:
    mid = (up + lo) / 2
    if pals[mid] < lower_bound: lo = mid
    else: up = mid
  if lower_bound <= pals[lo]: idx_lo = lo
  elif lower_bound <= pals[up]: idx_lo = up
  else: idx_lo = up + 1
  lo, up = 0, len(pals) - 1
  while up - lo > 1:
    mid = (up + lo) / 2
    if pals[mid] < upper_bound: lo = mid
    else: up = mid
  if upper_bound < pals[lo]: idx_up = lo - 1
  elif upper_bound < pals[up]: idx_up = lo
  else: idx_up = up
  return idx_up - idx_lo + 1

samples = int(sys.stdin.readline().rstrip())
for i in range(samples):
  line = sys.stdin.readline().rstrip()
  [lo, up] = line.split()
  print "Case #%d: %s" % (i+1, f(int(lo), int(up)))

