#!/usr/bin/python
import sys
import string
import copy

# Open in- and output files
f = "" if len(sys.argv) < 2 else sys.argv[1]
i = open(f, 'r')
o = open("%s.out" % f, 'w')

# Parse input file
cases = int(i.readline())

def calc_center(obj,xmin,xmax,ymin,ymax):
    mass_sum = 0
    point_sum = [0,0]
    
    for x in range(xmin,xmax+1):
        for y in range(ymin,ymax+1):
            if not ((x == xmin and y == ymin) or (x == xmin and y == ymax) or (x == xmax and y == ymin) or (x == xmax and y == ymax)):
              mass_sum += obj[x][y]
              point_sum[0] += float(obj[x][y]) * (x+0.5)
              point_sum[1] += float(obj[x][y]) * (y+0.5)
            
    center = [point_sum[0] / mass_sum, point_sum[1] / mass_sum]
    print center
    return center[0] == xmin + float(xmax-xmin+1) / 2 and center[1] == ymin + float(ymax-ymin+1) / 2

for case in range(1, cases + 1):  
  # chunks = i.readline().strip().split(" ")
  # OR
  # value = int(i.readline())
  R, C, D = i.readline().strip().split(" ")
  R = int(R)
  C = int(C)
  D = int(D)
  
  plate = [[0]*C for x in xrange(R)]
  
  for r in range(R):
    row = i.readline()
    for c in range(C):
        plate[r][c] = D + int(row[c])

  print plate
  

  
  largest_possible = min(R,C)
  
  w = largest_possible;
  anything = False
  while not anything and largest_possible >= 3:
    for row in range(0, R - largest_possible + 1):
      for col in range(0, C - largest_possible +  1):
        if not anything:
          anything |= calc_center(plate, row, row+largest_possible-1, col, col+largest_possible-1)
    largest_possible -= 1
    
  result = 'IMPOSSIBLE' if not anything else str(largest_possible+1)
  print largest_possible+1

  result = "Case #%i: %s" % (case, result)
  print result
  o.write("%s\n" % result)

# Close in- and output
i.close()
o.close()
