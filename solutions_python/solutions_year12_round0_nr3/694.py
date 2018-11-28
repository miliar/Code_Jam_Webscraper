#!/usr/bin/env python

import sys

num_lines = int(sys.stdin.readline())

for i in xrange(0,num_lines):
  sp_line = sys.stdin.readline().split(" ")
  start = int(sp_line[0])
  end = int(sp_line[1])
  paired_num = {}
  paired_count = 0
  for j in xrange(start, end):
    digits = str(j)
    for k in xrange(1,len(digits)):
      digits = digits[-1] + digits[0:-1]
      alt_num = int(digits)
      if alt_num >= start and alt_num <= end and alt_num > j:
        if (j,alt_num) in paired_num:
          continue
        paired_num[(j,alt_num)] = 1
        paired_count += 1
        #print "(%d,%d)" % (j,alt_num)
  sys.stdout.write("Case #%d: %d\n" % (i+1, paired_count))
