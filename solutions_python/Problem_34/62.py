#!/usr/bin/env python
import re

count = raw_input()
nums = count.split(' ')
L = eval(nums[0])
D = eval(nums[1])
N = eval(nums[2])
words = []
for i in range(D):
  word = raw_input()
  words += [word]

for i in range(N):
  pattern = raw_input()
  pattern = pattern.replace("(", "[")
  pattern = pattern.replace(")", "]")
  count = 0
  for word in words:
    pre = re.compile(pattern)
    if(pre.match(word)):
      count += 1
  print "Case #%d: %d" % (i+1, count)

