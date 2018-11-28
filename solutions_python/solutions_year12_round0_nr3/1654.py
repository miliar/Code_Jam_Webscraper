#!/usr/bin/python -u

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " infile"
  sys.exit()
infile = open(sys.argv[1], 'r')

debugprint = 0

def debug(str, lvl=5):
  if debugprint > lvl: print "[DEBUG]", str

def handleonecase(line1):
  count = 0
  A = int(line1[0])
  B = int(line1[1])
  for n in range(A, B):
    count += get_count_of_m(A, B, n)
  return count

def get_count_of_m(A, B, n):
  count = 0
  orig_n = n
  while(1):
    n = move_digit(n)
    debug(n)
    if(int(n) == orig_n):
      return count
    if(n[0] == '0'):
      continue
    if(int(n) < A):
      continue
    if(int(n) > B):
      continue
    if(int(n) < orig_n):
      continue
    if(len(n) != len(str(orig_n))):
      continue
    count += 1

def move_digit(n):
  str_n = str(n)
  str_n = str_n[1:] + str_n[0]
  return str_n

maxcases = 0
casenum = 0

line = infile.readline().strip()
maxcases = int(line)
while line:
  casenum = casenum + 1
  if casenum > maxcases: break
  line1 = infile.readline().strip().split()
#  line2 = infile.readline().strip().split()
  result = handleonecase(line1)
  print "Case #" + str(casenum) + ": " + str(result)




