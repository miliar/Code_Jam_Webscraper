import sys

def war(naomi, ken, n):
  score, k = 0, n
  for i in range(n-1, -1, -1):
    chosen = naomi[i]
    x = optimal_selection(ken, k, chosen)
    if x != None:
      del ken[x]
    else:
      score +=1
      del ken[0]
    del naomi[i]
    k -= 1
  return score

def dec_war(naomi, ken, n):
  score, k = 0, n
  for i in range(0, n):
    chosen = ken[0]
    x = optimal_selection(naomi, k, chosen)
    if x != None:
      score += 1
      del naomi[x]
    else:
      del naomi[0]
    del ken[0]
    k -= 1
  return score

# binary search
def optimal_selection(pin, n, x):
  l, r = 0, n-1
  while True:
    if r-l > 1:
      m = (l+r) / 2
      if x >= pin[m]:
        l = m
      else:
        r = m
    elif r-l == 1:
      if pin[l] > x:
        return l
      elif pin[r] > x:
        return r
      else:
        return None
    else:
      return l if pin[l] > x else None

n = int(input())
for i in range(1, n+1):
  k = int(input())
  x = sorted([float(b) for b in sys.stdin.readline().strip().split(" ")])
  y = sorted([float(b) for b in sys.stdin.readline().strip().split(" ")])
  r1 = dec_war(x[:], y[:], k)
  r2 = war(x[:], y[:], k)
  print "Case #%s: %s %s" % (i, r1, r2)
