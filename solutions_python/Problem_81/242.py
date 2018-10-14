#!/usr/bin/python

t = input()
from array import array
from itertools import repeat, ifilter, izip

def average(ls):
  return float(sum(ls)) / len(ls)

def wp_excluding(A, team_ex):
  return [
    float(wins[team] - (A[team][team_ex]=='1' and 1 or 0)) /
        (games_played[team] - 1)
    for team in xrange(n) if team != team_ex and A[team][team_ex] != '.']

for test in xrange(t):
  print 'Case #{0}:'.format(test+1)
  n = input()
  A = [raw_input() for i in xrange(n)]
  games_played = [len(filter(lambda x: x!='.', team)) for team in A]
  wins = [len(filter(lambda x: x=='1', team)) for team in A]
  wp = [float(w)/gp for (w,gp) in izip(wins, games_played)]
  # owp = avg(wp of opponents if don't count games they played against me)
  owp = [average(wp_excluding(A, team))
      for team in xrange(n)]
  # oowp = avg(owp of opponents)
  oowp = [
            average([owp[opponent] for opponent in xrange(n) if A[team][opponent] != '.'])
            for team in xrange(n)
         ]
  for rez in (a/4 + b/2  + c/4 for (a,b,c) in izip(wp, owp, oowp)):
    print '{0}'.format(rez)
  
