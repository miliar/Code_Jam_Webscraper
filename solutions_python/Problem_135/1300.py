#! /usr/bin/python

import sys

def solve(answer1, arr1, answer2, arr2):
  pos_card = set(arr1[answer1-1]) & set(arr2[answer2-1])
  if len(pos_card) == 0:
    return "Volunteer cheated!"
  elif len(pos_card) == 1:
    return pos_card.pop()
  else:
    return "Bad magician!"
      
fd = open(sys.argv[1])

num_cases = int(fd.readline())

for i in range(0, num_cases):
  answer1 = int(fd.readline())
  arr1 = []
  for j in range(4):
    a = fd.readline().strip().split(" ")
    arr1.append(a)
  answer2 = int(fd.readline())
  arr2 = []
  for j in range(4):
    a = fd.readline().strip().split(" ")
    arr2.append(a)
#  print answer1, arr1, arr2
  output = solve(answer1, arr1, answer2, arr2)
  print "Case #%d:" % (i+1), output

