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


def solve(n):
  lst = map(int, list(str(n)))
  l = len(lst)
  for i in xrange(1, l):
    if lst[i] < lst[i - 1]:
      for x in xrange(i, l): lst[x] = 9
      j = i - 1
      lst[j] -= 1
      while j > 0:
        if lst[j] < lst[j - 1]:
          lst[j] = 9
          lst[j - 1] -= 1
        j -= 1
      if lst[0] <= 0: lst = lst[1:]
      return int("".join(map(str,lst)))
  return n


result = []
T = ri()
for x in xrange(T):
  n = ri()
  result.append("Case #%s: %s" % (x+1, solve(n)))
with open("./bres", "w+") as f:
    f.write("\n".join(result))



# print solve(132)
# print solve(1000)
# print solve(7)
# print solve(111111111111111111)

# def simple(n):
#   def check(k):
#     digs = map(int, list(str(k)))
#     l = len(digs)
#     for i in xrange(1, l):
#       if digs[i-1] > digs[i]: return False
#     return True
#   while check(n) == False:
#     n -= 1
#   return n


# for x in xrange(10000):
#   smx = simple(x)
#   slx = solve(x)
#   if slx != smx:
#     print x, slx, smx, slx == smx