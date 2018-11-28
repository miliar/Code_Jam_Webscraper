#!/usr/bin/python

import sys

class CaseIt(object):
  def __init__(self, f):
    self.f = f
    self.T = int(self.f.readline())
    self.cases_left = self.T

  def __iter__(self):
    for i in xrange(self.cases_left):
      N = self.f.readline()
      lines = []
      for i in xrange(int(N)):
        lines.append(self.f.readline())
      yield lines

def get_totals(i):
  totals = []
  WP = []
  for team in i:
    win = 0
    loss = 0
    for game in team:
      if game == '0':
        loss += 1
      elif game == '1':
        win += 1
    totals.append((win, loss))
    WP.append(float(win)/float(win+loss))

  return (totals, WP)

def get_OWP(i, record):
  OWPL = []
  for team in i:
    OWP = []
    for game_i in xrange(len(team)):
      game = team[game_i]

      if game == '0':
        OW = record[game_i][0] - 1
        OP = record[game_i][0] + record[game_i][1] - 1
        OWP.append(float(OW)/float(OP))
      elif game == '1':
        OW = record[game_i][0]
        OP = record[game_i][0] + record[game_i][1] - 1
        OWP.append(float(OW)/float(OP))
    OWPL.append(avg(OWP))

  return OWPL

def get_OOWP(i, OWP):
  OOWPL = []
  for team in i:
    OOWP = []
    for game_i in xrange(len(team)):
      game = team[game_i]

      if game == '0' or game == '1':
        OOWP.append(OWP[game_i])
    OOWPL.append(avg(OOWP))

  return OOWPL

def avg(l):
  return float(sum(l)) / float(len(l))

def solve(i):
  (record, WP) = get_totals(i)

  OWP = get_OWP(i, record)

  OOWP = get_OOWP(i, OWP)

  for (wp, owp, oowp) in zip(WP, OWP, OOWP):
    print wp * 0.25 + owp * 0.5 + 0.25 * oowp

def main(filename):
  f = open(filename, "r")


  case = 1
  for i in CaseIt(f):
    print "Case #" + str(case) + ":"

    solve(i)

    case += 1

if __name__ == "__main__":
  main(sys.argv[1])
