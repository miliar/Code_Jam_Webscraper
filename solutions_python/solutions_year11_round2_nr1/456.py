#!/usr/bin/python

import sys

total = int(sys.stdin.readline())

for tournament in range(total):
  print "Case #%s:" % (tournament+1)

  results = []
  wp = []
  owp = []
  oowp = []
  teamcount = int(sys.stdin.readline())
  for team in range(teamcount):
    result = sys.stdin.readline().strip()
    results.append(result)
    wins = result.count('1')
    losses = result.count('0')
    wp.append(1.0*wins/(wins+losses))

  for team in range(teamcount):
    owpTotal = 0
    opponentCount = 0
    for opponent in range(teamcount):
      if results[team][opponent]=='.':
        continue
      opponentCount += 1
      result = results[opponent][:team] + results[opponent][team+1:]
      wins = result.count('1')
      losses = result.count('0')
      owpTotal += 1.0*wins/(wins+losses)
    owp.append(owpTotal/(opponentCount))

  for team in range(teamcount):
    oowpTotal = 0
    opponentCount = 0
    for opponent in range(teamcount):
      if results[team][opponent]=='.':
        continue
      opponentCount += 1
      oowpTotal += owp[opponent]
    oowp.append(oowpTotal/opponentCount)

  for team in range(teamcount):
    print (0.25 * wp[team] + 0.50 * owp[team] + 0.25 * oowp[team])

  #print wp
  #print owp
  #print oowp
