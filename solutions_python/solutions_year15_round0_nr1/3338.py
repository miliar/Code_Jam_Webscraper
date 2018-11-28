#!/usr/bin/python

import sys

# how to use it:
# python solution.py test

def init():
  # print 'Number of arguments:', len(sys.argv), 'arguments.'
  # print 'Argument List:', str(sys.argv)

  f = open(sys.argv[1], 'r')

  cases = int(f.readline())

  for case in xrange(cases):
    problem = f.readline()[:-1].split(' ') # remove \n
    solveStandingOvation(case, int(problem[0]), problem[1])

def solveStandingOvation(case, levels, people):
  attending = 0
  invites = 0

  for l in xrange(levels+1):
    additional = l - attending - invites
    if additional > 0:
      invites = invites + additional
    attending = attending + int(people[l])

  print 'Case #' + str(case+1) + ': ' + str(invites)

init()
