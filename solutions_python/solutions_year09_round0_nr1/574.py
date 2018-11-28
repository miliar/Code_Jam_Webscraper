#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re

def match(word, test):
  result = True
  if len(word) != len(test):
    result = False
  for i in range(0, len(word)):
    current = test[i]
    if current.find(word[i]) < 0:
      result = False
      break
  return result

def reg_match(word, tess):
  regex_str = ""
  for case in test:
    regex_str += "[" + case + "]"
  regex = re.compile(regex_str)
  result = regex.match(word)
  return True if result != None else False

def out_tests(tests):
  for test in tests:
    line = ""
    for case in test:
      if len(case) == 1:
        line += case
      else:
        line += '(' + case + ')'
    print line

nums = sys.stdin.readline().strip().split(' ')
L = int(nums[0])
D = int(nums[1])
N = int(nums[2])

dic = []
for i in range(0, D):
  dic.append(sys.stdin.readline().strip())

tests = []
for i in range(0, N):
  case = []
  pattern = sys.stdin.readline().strip()
  index = 0
  while index < len(pattern):
    c = pattern[index]
    if c != '(':
      case.append(c)
      index += 1
    else:
      group = pattern[index + 1 : pattern.find(')', index + 1)]
      case.append(group)
      index += len(group) + 2
  tests.append(case)

results = []
for test in tests:
  count = 0
  for word in dic:
    if match(word, test):
#    if reg_match(word, test):    
      count += 1
  results.append(count)

for i in range(0, len(results)):
  print "Case #%(index)d: %(count)d" % {'index':i+1, 'count':results[i]}
