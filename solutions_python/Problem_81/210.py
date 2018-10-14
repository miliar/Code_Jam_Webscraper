#!/usr/bin/python
import reader
import sys
class tourn :
  def __init__(self, nTeams) :
    self.teams = [team(nTeams, i) for i in range(nTeams)]
    for tm in self.teams : 
      tm.setTeams(self.teams)
  def __str__(self) :
    return "\n".join(str(team) for team in self.teams)

class team :
  def __init__(self, nTeams, num) :
    self.record = ["." for i in range(nTeams)]
    self.num = num
    self.wp = -1 
    self.owp = -1 
    self.oowp = -1

  def setTeams(self, teams) : 
    self.teams = teams

  def __str__(self) :
    return chr(self.num/26 + 65) + chr(self.num%26+65) + "|" + "".join(self.record)

  def getOps(self) : 
    ops = [i for i in range(len(self.record)) if not self.record[i] == '.']
    self.nOps = len(ops) * 1.0
    return ops

  def getWP(self) : 
    if self.wp == -1 : 
      self.wp = sum(1 for i in self.getOps() if self.record[i] == '1') / self.nOps 
    return self.wp

  def getTWP(self, throwout) :
    return sum(1 for i in range(len(self.record)) if ((self.record[i] == '1' )and (not i == throwout))) / (1.0 * sum(1 for i in range(len(self.record)) if ((not self.record[i] == '.') and (not i == throwout))))

  def getOWP(self) : 
    if self.owp == -1 : 
      self.owp = sum(self.teams[i].getTWP(self.num) for i in self.getOps()) / self.nOps
    return self.owp

  def getOOWP(self) :
    return sum(self.teams[i].getOWP() for i in self.getOps()) / self.nOps

  def getRPI(self) :
    return self.getWP()*0.25 + self.getOWP() * 0.5 + self.getOOWP() * 0.25

def solve(inputString, err=sys.stderr, out=sys.stdout) :
  lines = inputString.split("\n")
  nCases = int(lines[0])
  lineNo = 1
  rounds = []
  for case in range(1,nCases+1) :
    nTeams = int(lines[lineNo])
    trn = tourn(nTeams)
    lineNo += 1
    err.write("Case #%d\n" % case)
    for team in range(nTeams) :
      wins = lines[lineNo+team] 
      for i in range(nTeams) : 
        trn.teams[team].record[i] = wins[i]
    out.write("Case #%d:\n"%case)
    for i in range(nTeams) :
      team = trn.teams[i]
      err.write("Team #%d WP: %f\n" % (i, team.getWP()))
      err.write("Team #%d OWP: %f\n" % (i, team.getOWP()))
      err.write("Team #%d OOWP: %f\n" % (i, team.getOOWP()))
      out.write("%f\n" % (team.getRPI())) 
    err.write(str(trn) + "\n")
    lineNo += nTeams
inputs = [inpt for inpt in reader.getAll()]
for problem in inputs :
  solve(problem.string, err=sys.stdout, out=problem.f)
