#!/usr/bin/python
import sys

def calc(lines):
  lines = list(lines)
  if len(lines) == 1:
    return lines[0]
  if len(lines) == 0:
    return "Volunteer cheated!"
  return "Bad magician!"

def main():
  d = file(sys.argv[1]).readlines()
  n = int(d[0])
  for j in xrange(n):
    curr = 1 + j*10
    first = int(d[curr])
    first_line_nums = set(d[curr+first].split())
    curr += 5
    second = int(d[curr])
    second_line_nums = set(d[curr+second].split())
    total = first_line_nums & second_line_nums
    print "Case #%d: %s" % (j+1, calc(total))

main()
