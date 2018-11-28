#! /usr/bin/env python

import sys

T = int(raw_input())

for test in xrange(T):
  first_row = int(raw_input())
  first = []
  
  for i in xrange(4):
    first.append( [int(x) for x in raw_input().split()] )
  
  first = first[first_row - 1]
  
  second_row = int(raw_input())
  second = []
  
  for i in xrange(4):
    second.append( [int(x) for x in raw_input().split()] )
  
  second = second[second_row - 1]
  
  cnt = 0
  ans = -1

  for elem in first:
    if elem in second:
      cnt += 1
      if ans == -1:
        ans = elem

  if cnt == 0:
    print "Case #%d: Volunteer cheated!" % (test + 1)
  elif cnt == 1:
    print "Case #%d: %d" %(test + 1, ans)
  else:
    print "Case #%d: Bad magician!" % (test + 1)

