import copy
import itertools
from collections import defaultdict
import math
def key_func(a):
  return a[3]
def comp_pancake(a,b):
  if a[3] > b[3]:
    return 1
  elif a[3] < b[3]:
    return -1
  else:
    return 0
t = int(input())  # read a line with a single integer
for case in range(1, t + 1):
  n,k = [(int(s)) for s in input().split(' ')]
  pancake = []
  rad = [] 
  hei = []
  surface = []
  side = []
  for i in range(n):
    r,h = [(int(s)) for s in input().split(' ')]
    surface = r*r*math.pi
    side = 2*r*math.pi*h
    pancake.append((r,h,surface,side,i))
    #rad.append(r)
    ##hei.append(h)
    #surface.append(r*r*math.pi)
    #side.append(2*r*math.pi*h)
  max_bottom = 0
  max_total = 0
  pancake_sorted = sorted(pancake,key=key_func,reverse=True)
  for i in range(n):
    bottom = pancake[i][2] + pancake[i][3]
    total = bottom
    count = 1
    if (k > count):
      for j in range(n):
        if (pancake_sorted[j][0] <= pancake[i][0]) and\
           (pancake_sorted[j][4] != pancake[i][4]):
          total += pancake_sorted[j][3]
          count += 1
          if (count == k):
            break
    if (count == k):
      if (total > max_total):
        max_total = total
  res_str = "%f" %max_total
  case_str = "Case #%d: " %case
  print(case_str + res_str)
  #print case_str + "%d,%d" %(max_circle,max_pair_circle)
