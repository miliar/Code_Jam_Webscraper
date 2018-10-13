#!/usr/bin/python

from __future__ import division

import sys

def readInput():
  file = open(sys.argv[1])

  testCaseCount = int(file.readline())

  testCases = [[file.readline().rstrip() for x in xrange(int(file.readline()))] for a in xrange(testCaseCount)]
  
  return testCases

def solve(data):
  teams = len(data)

  gamesPlayed = [len([a for a in x if a != '.']) for x in data]
  gamesWon = [len([a for a in x if a == '1']) for x in data]


  wp = [gamesWon[x] / gamesPlayed[x] for x in xrange(teams)]
  wpwon = [(gamesWon[x] - 1) / (gamesPlayed[x] - 1) for x in xrange(teams)]
  wplost = [gamesWon[x] / (gamesPlayed[x] - 1) for x in xrange(teams)]

  owp = []
  for x in data:
    opponents = [a for a in xrange(teams) if x[a] != '.']
    owpsum = 0
    for opponent in opponents:
      if x[opponent] == '0':
        owpsum += wpwon[opponent]
      else:
        owpsum += wplost[opponent]

    owp.append(owpsum / len(opponents))

  oowp = []
  for x in data:
    opponents = [a for a in xrange(teams) if x[a] != '.']
    oowpsum = 0
    for opponent in opponents:
      oowpsum += owp[opponent]

    oowp.append(oowpsum / len(opponents))

  scores = [wp[x] / 4 + owp[x] / 2 + oowp[x] / 4 for x in xrange(teams)]
    
  return scores

testCases = readInput()

testCaseNr = 1
for testCase in testCases:
  print 'Case #%d:' % testCaseNr
  for line in solve(testCase):
    print line
  testCaseNr += 1
