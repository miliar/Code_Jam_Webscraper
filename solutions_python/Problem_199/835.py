import sys, math
def rs():
    return sys.stdin.readline().strip()
def ri():
    return int(sys.stdin.readline().strip())
def ras():
    return list(sys.stdin.readline().strip())
def rai():
    return map(int,sys.stdin.readline().strip().split())
def raf():
    return map(float,sys.stdin.readline().strip().split())


def solve(s, k):
  lst = map(lambda x: 0 if x == '-' else 1, list(s))
  l = len(lst)
  count = 0
  for i in xrange(l - k + 1):
    if lst[i] == 0:
      count += 1
      for j in xrange(i, i + k):
        lst[j] = 1 - lst[j]
  if sum(lst) == len(lst): return count
  else: return "IMPOSSIBLE"


result = []
T = ri()
for x in xrange(T):
  s, k = sys.stdin.readline().strip().split()
  k = int(k)
  result.append("Case #%s: %s" % (x+1, solve(s, k)))
with open("./ares", "w+") as f:
    f.write("\n".join(result))
