import heapq
import copy

cases = int(raw_input())

for case in xrange(cases):
  total = int(raw_input())
  naomi = raw_input().split()
  naomi.sort()
  n2 = copy.deepcopy(naomi)
  ken = raw_input().split()
  ken.sort()
  k2 = copy.deepcopy(ken)

  num = 0
  n = float(ken.pop(0))
  while True:
    try:
      k = float(naomi.pop(0))
      if n < k:
        num = num + 1
        n = float(ken.pop(0))
    except:
      break
  print "Case #" + str(case+1) + ": " + str(num),

  sec = 0
  n = float(n2.pop(0))
  while True:
    try:
      k = float(k2.pop(0))
      if n < k:
        sec = sec + 1
        n = float(n2.pop(0))
    except:
      break
  print total - sec

"""while True:
    try:
      print heapq.heappop(naomi),
    except:
      break

print ""
while True:
    try:
      print heapq.heappop(ken),
    except:
      break"""
