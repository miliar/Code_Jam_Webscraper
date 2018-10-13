import math

t = int(raw_input())

for i in xrange(1, t + 1):
  
  n,k = [int(v) for v in raw_input().split(" ")]
  area = 0.0
  result = 0.0

  arr = [None]*n
  for j in xrange(0,n):
    r,h = [long(v) for v in raw_input().split(" ")]
    arr[j] = (r,h)

  arr.sort(reverse = True)
  
  for t in xrange(0,n-k+1):
    area = math.pi * arr[t][0] * arr[t][0] + 2 * math.pi * arr[t][0] * arr[t][1] 
    hh = arr[t+1:]
    hh.sort(reverse = True,key=lambda tup: tup[0] * tup[1])
    for w in xrange(0,k-1):
      area += 2 * math.pi * hh[w][0] * hh[w][1]
    if (area > result):
      result = area

  print "Case #{}: {}".format(i, result)
