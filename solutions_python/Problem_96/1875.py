#!/usr/bin/env python2

count = int(raw_input())

def safe_sub(num,suber):
  num2 = num - suber
  if num2 <= 0:
    return 0
  else:
    return num2

for x in xrange(1,count+1):
  inputs = raw_input().split(" ")
  num_count = int(inputs[0])
  num_surp = int(inputs[1])
  best_rest = int(inputs[2])
  scores = inputs[3:]
  result = 0
  for y in xrange(0,len(scores)):
    scores[y] = int(scores[y])
  for y in scores:
    if safe_sub(best_rest*3,4) > y or (y == 0 and best_rest != 0):
      continue
    if safe_sub(best_rest*3,2) <= y:
      result += 1
    elif safe_sub(best_rest*3,4) <= y and num_surp > 0:
      num_surp -= 1
      result += 1
  print "Case #" + str(x) + ": " + str(result)
