import sys, math
import heapq

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


def solve(n, k):
  mp = {-n: 1}
  heap = []
  heapq.heappush(heap, -n)
  count = 0
  while True:
    v = heapq.heappop(heap)
    count += mp[v]
    if count >= k: return " ".join([str(abs(v) / 2), str((abs(v) - 1) / 2)])
    else:
      a,b = -1 * (abs(v) / 2), -1 * ((abs(v) - 1) / 2)
      if not(a in mp): heapq.heappush(heap, a)
      mp[a] = mp.get(a, 0) + mp[v]
      if not(b in mp): heapq.heappush(heap, b)      
      mp[b] = mp.get(b, 0) + mp[v]

result = []
T = ri()
for x in xrange(T):
  n,k = rai()
  result.append("Case #%s: %s" % (x+1, solve(n,k)))
with open("./cres", "w+") as f:
    f.write("\n".join(result))


# def simple(n, k):
#   heap = []
#   heapq.heappush(heap, -n)
#   for i in xrange(k-1):
#     v = heapq.heappop(heap)
#     a,b = -1 * (abs(v) / 2), -1 * ((abs(v) - 1) / 2)
#     heapq.heappush(heap, a)
#     heapq.heappush(heap, b)
#   v = heapq.heappop(heap)
#   return ', '.join([str(abs(v) / 2), str((abs(v) - 1) / 2)])


# T = ri()
# for x in xrange(T):
#   n,k = rai()
#   slv = solve(n,k)
#   sml = simple(n,k)
#   print n,k, '--->', slv
#   if sml != slv: print "!!!!!"


# import random as rd
# for x in xrange(1000):
#   n = rd.randint(1, 1000)
#   k = rd.randint(1, n)
#   slv = solve(n,k)
#   sml = simple(n,k)
#   if slv != sml: print n,k
#   # print n,k, slv, sml, slv == sml

# print solve(4, 2) == simple(4,2)
# print solve(5, 2)
# print solve(6, 2)
# print solve(1000, 1000)
# print solve(1000, 1)
# print solve(7, 5)
# print solve(10**6, 10**6)



