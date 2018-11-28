#!/usr/bin/python

from __future__ import with_statement
from string import atoi

def countSameEls(lst, el):
  j = 0
  for i in lst:
    if (i ==el):
      j = j+1
  return j

def findEl(lst, start, value):
  for i in xrange(start, len(lst)):
    if (lst[i] == value):
      return i
  return -1


with open("large.in") as input:
  exampleNum = atoi(input.readline())

  for i in xrange(1, exampleNum + 1):
    engineNum = atoi(input.readline())
    engines = []
    for j in xrange(0, engineNum):
      engines.append(input.readline()[:-1])

    queryNum = atoi(input.readline())
    queries = []
    for j in xrange(0, queryNum):
      queries.append(input.readline()[:-1])

    if (len([val for val in engines if val in queries]) == 0):
      print "Case #" + str(i) + ": 0"
    elif (len([val for val in engines if val not in queries]) > 0):
      print "Case #" + str(i) + ": 0"
    else:
      num = 0
      q = 0
      while (q != queryNum):
        bst = q
        for z in xrange(0, engineNum):
	  fel = findEl(queries, q, engines[z])
	  if (fel == -1):
            bst = queryNum
          elif (fel > bst):
	    bst = fel
        if (q > 0 ):
          num = num + 1
	q = bst
      print "Case #" + str(i) + ": " + str(num)