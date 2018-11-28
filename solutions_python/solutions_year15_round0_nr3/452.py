#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

count = None
num_repeats = None
tests = []

reverse_labels = {"1":1,"i":2,"j":3,"k":4}

for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  elif not num_repeats:
    length, num_repeats = tuple([int(x) for x in line.strip().split(" ")])
  else:
    s = line.strip()
    if len(s) != length:
      print "Wrong string length on line:", line
      sys.exit(0)
    tests.append([reverse_labels[x] for x in s] * num_repeats)
    num_repeats = None

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

labels = [None,"1","i","j","k"]
reverse_labels = {"1":1,"i":2,"j":3,"k":4}
mult_table = [
[1,2,3,4],
[2,-1,4,-3],
[3,-4,-1,2],
[4,3,-2,-1],
]

def label_string(s):
  return "".join(labels[x] for x in s)

def q_mult(x,y):
  sign = 1
  if x < 1:
    sign *=-1
  if y < 1: 
    sign *=-1

  return sign * mult_table[abs(x)-1][abs(y)-1]

def solve_1(s):
  result = 1
  for i in range(len(s)):
    result = q_mult(result, s[i])

  if result > 0 and result == 4:
    #print "%s == k" % s
    return True
  return False

def solve_2(s):
  result = 1

  for i in range(len(s)):
    result = q_mult(result, s[i])
    if result == 3 and solve_1(s[i+1:]):
      #print "%s == j" % s[:i+1]
      return True
  return False

def solve_3(s):
  result = 1

  for i in range(len(s)):
    result = q_mult(result, s[i])
    if result == 2 and solve_2(s[i+1:]):
      #print "%s == i" % s[:i+1]
      return True
  return False

def solve(s):
  
  i_end = 0
  i_buf = 1
  while i_end < len(s)-2:
    i_buf = q_mult(i_buf, s[i_end])
    i_end += 1
    if i_buf == 2:
      j_end = i_end
      j_buf = 1
      while j_end < len(s)-1:
        j_buf = q_mult(j_buf, s[j_end])
        j_end += 1
        if j_buf == 3:
          k_buf = 1
          k_end = j_end
          while k_end < len(s):
            k_buf = q_mult(k_buf, s[k_end])
            k_end += 1
          if k_buf == 4:
            #print label_string(s[:i_end]), label_string(s[i_end:j_end]), label_string(s[j_end:])
            return True

def linear_solve(s):
  
  current = 1
  seen = 0
  for i in range(len(s)):
    current = q_mult(current, s[i])
    if seen == 0 and current == 2:
      seen += 1
      current = 1
    elif seen == 1 and current == 3:
      seen += 1
      current = 1

  return current == 4 and seen == 2
    
counter = 0
for t in tests:
  counter += 1
  #print t
  print "Case #%d: %s" % (counter, "YES" if linear_solve(t) else "NO")
#print tests




