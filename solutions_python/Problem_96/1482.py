#!/usr/bin/python2.6
import sys
filez = open(sys.argv[1], 'r')
n_lines = int(filez.readline())
for bi in range(0, n_lines):
  print 'Case #%d:' % (bi + 1),
  line = filez.readline()
  fields = map(int,line.split())
  num_googlers = int(fields[0])
  surprises = int(fields[1])
  min_score = int(fields[2])
  total = 0
  for score in fields[3:]:
    if min_score == 0:
      total += 1
      continue
    if min_score == 1:
      if score >= 1:
        total += 1
      continue
    if min_score == 2:
      if score >= 4:
        total += 1
        continue
      if score >= 2:
        if surprises > 0:
          surprises -=1
          total +=1
      continue
      
    if (score <= min_score):
      continue
    if (score / min_score) >= 3:
      total += 1
      continue
    if (score - min_score) / (min_score - 1) >= 2:
      total += 1
      continue
    if (score - min_score) / (min_score - 2) >= 2:
      if surprises > 0:
        surprises -= 1
        total += 1
  print total
