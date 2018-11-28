#! /usr/bin/env python
import sys

testcases = int(sys.stdin.readline())
case = 1
while case <= testcases:
  first_ans_row = int(sys.stdin.readline())
  first_ans = None
  for line_n in xrange(1, 5):
    line = sys.stdin.readline()
    if line_n == first_ans_row:
      first_ans = { int(a) for a in line.split() }

  second_ans_row = int(sys.stdin.readline())
  second_ans = None
  for line_n in xrange(1, 5):
    line = sys.stdin.readline()
    if line_n == second_ans_row:
      second_ans = { int(a) for a in line.split() }
  
  cards = first_ans & second_ans
  if len(cards) == 0:
    print "Case #%d: Volunteer cheated!" % (case,)
  elif len(cards) == 1:
    print "Case #%d: %d" % (case, cards.pop())
  else:
    print "Case #%d: Bad magician!" % (case,)

  case += 1
