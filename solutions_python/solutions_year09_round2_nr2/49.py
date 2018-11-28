#!/usr/bin/env python

import sys

infile = open(sys.argv[1], 'r')
outfile = open("%s.out" % sys.argv[1], 'w')

tests = int(infile.readline().strip())

def tokenize(i):
  res = []
  while(i > 0):
    res.insert(0, i % 10)
    i /= 10
  return res

def mjoin(lst):
  """Turns a list of numbers back into one number"""
  val = 0
  for item in lst:
    val = val * 10 + item
  return val

def new_smallest(lst):
   min = 999
   pos = -1
   for i in range(0, len(lst)):
      if lst[i] < min and lst[i] > 0:
         min = lst[i]
         pos = i
         # print "new min: %d found at: %d" % (min, pos)
   # remove min value
   # print "      pos: %d" % pos
   # print "  up list: %s" % lst[:pos]
   # print "   d list: %s" % lst[pos+1:]
   nlst = lst[:pos] + lst[(pos+1):]
   # print "   min: %d" % min
   # print "  nlst: %s" % nlst
   res = [min, 0]
   nlst.sort()
   res += nlst
   return res

# print new_smallest([3,2,1])
# print new_smallest([3,2,0,1])
# print new_smallest([3,2,0,1,0])

def perform(nums):
   """Find the first position where a number is smaller than one 
      that comes before it"""
   nums.reverse()
   pos = 0
   last = 0
   ## Find first point where a digit is is large than
   ## ones that comes later, that's the operating string
   for i in range(1,len(nums)):
     if nums[i-1] > nums[i]:
        pos = i + 1
        last = nums[i]
        break
   stay = nums[pos:]
   op   = nums[:pos]
   # print "   stay: %s" % stay
   # print "     op: %s" % op
   ## find smallest value larger than pivot point
   min = 999
   min_pos = 0
   for i in range(0,len(op)):
      if op[i] < min and op[i] > last:
        min_pos = i
        min = op[i]
   if min == 999:
      # print "no min found, returning input"
      # nums.reverse()
      ## cycle back to beginning?
      res = new_smallest(nums)
      return res
   # print "   min: %d" % min
   op = op[:min_pos] + op[min_pos+1:]
   stay.reverse()
   stay.append(min)
   op.sort()
   # print "   stay: %s" % stay
   # print "     op: %s" % op
   nums = stay + op
   return nums

def calc_next(val):
  nums = tokenize(val)
  # print nums
  lst = perform(nums)
  return mjoin(lst)

case = 1
for line in infile:
  val = int(line)
  res = calc_next(val)
  print "Case #%d: %d" % (case, res)
  case += 1

