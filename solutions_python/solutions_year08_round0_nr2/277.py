#!/usr/bin/python

from __future__ import with_statement
from string import atoi

def findMinStartByEnd(table, direction, start, timeout):
  for m in xrange(0, len(table[not direction])):
    if table[not direction][m][0] >= (table[direction][start][1] + timeout):
      return m
  return -1

def findDirection(AB, BA):
  return (not (AB[0][0] <= BA[0][0]))

with open("B-large.in") as input:
  exampleNum = atoi(input.readline())

  for i in xrange(1, exampleNum + 1):
    timeout = atoi(input.readline())

    [NA, NB] = input.readline().split(" ")
    [NA, NB] = [atoi(NA), atoi(NB)]

    table = [[],[]]
    for j in xrange(0, NA):
      [tS, tE] = input.readline().split(" ")
      [tS, tE] = [tS.split(":"), tE.split(":")]
      [tS, tE] = [atoi(tS[0])*60 + atoi(tS[1]), atoi(tE[0])*60 + atoi(tE[1])]
      table[0].append([tS, tE]);

    for j in xrange(0, NB):
      [tS, tE] = input.readline().split(" ")
      [tS, tE] = [tS.split(":"), tE.split(":")]
      [tS, tE] = [atoi(tS[0])*60 + atoi(tS[1]), atoi(tE[0])*60 + atoi(tE[1])]
      table[1].append([tS, tE]);

    table[0].sort(key=lambda a: a[0])
    table[1].sort(key=lambda a: a[0])

    RESULT = [0, 0]
    loop = True;
    while loop:
      if ((len(table[0]) == 0) or (len(table[1]) == 0)):
        print "Case #" + str(i) + ": " + str(len(table[0]) + RESULT[0]) + " " + str(len(table[1]) + RESULT[1])
	loop = False

      else:
        direction = findDirection(table[0], table[1])
	RESULT[direction] = RESULT[direction] +1;
	start = 0
	while (start != -1):
          nstart = findMinStartByEnd(table, direction, start, timeout)
	  table[direction].pop(start)
	  direction = not direction
	  start = nstart