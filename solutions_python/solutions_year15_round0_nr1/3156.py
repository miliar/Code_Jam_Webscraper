#!/usr/bin/python

import sys

input = open(sys.argv[1])

numCases = int(input.readline().strip())

for i in range(numCases):
  line = input.readline().strip()
  seq = line.split()[-1]
  seq = list(seq)
  seq = [int(n) for n in seq]

  numPpl = 0
  numInvite = 0

  for level in range(len(seq)):
    if numPpl >= level:
      numPpl += seq[level]
    else:
      numInvite += (level - numPpl)
      numPpl = level + seq[level]

  print "Case #" + str(i+1) + ": " + str(numInvite)
