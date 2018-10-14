import heapq

def init2(n):
  stalls = [False] * n
  ls = range(n)
  rs = range(n-1, -1, -1)
  return stalls, ls, rs

def init(n):
  extents = []
  heapq.heappush(extents, (-n, 0))
  return extents

def place(extents):
  xt = heapq.heappop(extents)

  largest = -xt[0]
  largest_idx = xt[1]

  new_ls = (largest - 1) / 2 # 1 -> 0, 2 -> 0, 3 -> 1, 4 -> 1, 5 -> 2
  new_rs = largest - new_ls - 1 # 1 -> 0, 2 -> 1, 3 -> 1, 4 -> 2, 5 -> 2
  # -3, 0 -> (-1, 0); (-1, 2)
  if new_ls > 0:
    heapq.heappush(extents, (-new_ls, largest_idx))
  if new_rs > 0:
    heapq.heappush(extents, (-new_rs, largest_idx + new_ls + 1))
  return (new_ls, new_rs)


def sim(n, k):
  i = 1
  prevacc = 0
  acc = 0
  while acc < n:
    prevacc = acc
    acc += i
    i = i * 2
  if prevacc <= k:
    return (0, 0)
  return None

def get_x(n):
  x = 0
  while True:
    if 2**x - 1 < n <= 2**(x + 1) - 1:
      return x
    x = x + 1

def calc(n, k):
  x = get_x(n)
  lim = 2**x - 1
  if k > lim:
    return (0, 0)
  # else calculate next step
  n_over = n - lim
  # ls rs
  # e.g. x = 3, n_over = 7 ; exts = 
  k = lim - k

  half = 2**(x - 1)
  exts = distribute(n_over, half)
  return lookup(k, exts)

def lookup(k, exts):
  while k >= exts[1]:
    k -= exts[1]
    exts = collapse(exts)
  sumof, over = exts
  base = sumof / (over * 2)
  with_more = sumof % (over * 2)
  result = [base, base]
  if with_more > over and (over - k) <= (with_more - over):
      result[0] += 1
  if with_more > over or (over - k) <= with_more:
      result[1] += 1
  return result

def distribute(n_over, half):
  return (n_over, half)

def collapse(exts):
  sumof, orig_len = exts
  half = orig_len / 2
  s = sumof + orig_len
  return (s, half)
  


"""
for i in range(10, 15):
  print i
  extents = init(i)
  for j in range(i):
    ls, rs = place(extents)
    lls, rrs = calc(i, j + 1)
    print ">> ", ls, rs, lls, rrs


for 2^x -1 < n <= 2^(x+1) - 1
then sim(n, k) = (0, 0) when k > 2^x - 1
1 1 - 0 0 x=0, k must > 0
2 1 - 0 1 x=1, k must > 1
2 2 - 0 0
3 1 - 1 1 x=1, k must > 1
3 2 - 0 0
3 3 - 0 0
4 1 - 1 2 x=2, k must > 3
4 2 - 0 1
4 3 - 0 0
4 4 - 0 0
5 1 - 2 2 x=2, k must > 3
5 2 - 0 1
5 3 - 0 1
5 4 - 0 0
5 5 - 0 0
"""

t = int(raw_input())
for c in xrange(1, t+1):
  n, k = (int(c) for c in raw_input().split())
  # print n, k
  ls, rs = calc(n, k)
  print "Case #{}: {} {}".format(c, max(ls, rs), min(ls, rs))
