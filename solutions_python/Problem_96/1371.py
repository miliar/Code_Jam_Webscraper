#!/usr/bin/env python
import sys
import pprint
from sets import Set

class Score:
  def __init__(self, scoreTotal):
    self.scoreTotal = scoreTotal

  def possibleSetsOfScores(self):
    avgScore = self.scoreTotal/3

    if (self.scoreTotal % 3 == 0):
      if (avgScore == 0):
        return [[avgScore, avgScore, avgScore]]
      else:
        return [[avgScore, avgScore, avgScore], [avgScore-1, avgScore, avgScore+1]]

    if (self.scoreTotal % 3 == 1):
      if (avgScore == 0):
        return [[avgScore, avgScore, avgScore+1]]
      else:
        return [[avgScore, avgScore, avgScore+1], [avgScore-1, avgScore+1, avgScore+1]]

    if (self.scoreTotal % 3 == 2):
      return [[avgScore, avgScore, avgScore+2], [avgScore, avgScore+1, avgScore+1]]

    # this shouldn't happen
    return None

  def surprisingScore(self):
    avgScore = self.scoreTotal/3

    if (self.scoreTotal % 3 == 0):
      if (avgScore == 0):
        return self.regularScore()
      else:
        return [avgScore-1, avgScore, avgScore+1]

    if (self.scoreTotal % 3 == 1):
      if (avgScore == 0):
        return self.regularScore()
      else:
        return [avgScore-1, avgScore+1, avgScore+1]

    if (self.scoreTotal % 3 == 2):
      return [avgScore, avgScore, avgScore+2]

    # this shouldn't happen
    return None

  def regularScore(self):
    avgScore = self.scoreTotal/3

    if (self.scoreTotal % 3 == 0):
      return [avgScore, avgScore, avgScore]

    if (self.scoreTotal % 3 == 1):
      return [avgScore, avgScore, avgScore+1]

    if (self.scoreTotal % 3 == 2):
      return [avgScore, avgScore+1, avgScore+1]

    # this shouldn't happen
    return None

class ScoreCollection:
  def __init__(self, numOfGooglers, numOfSurprisingTriplets, p, scoreTotals):
    self.numOfGooglers = numOfGooglers
    self.numOfSurprisingTriplets = numOfSurprisingTriplets
    self.p = p
    self.scoreTotals = scoreTotals
    self.actualScores = []
    
    assert (self.numOfGooglers == len(self.scoreTotals)), "num of googlers (%d) doesn't match number of scores (%d)" % (self.numOfGooglers, len(self.scoreTotals))

  @staticmethod
  def makeFromInputStr(inputStr):
    data = inputStr.split(' ')

    assert (len(data) >= 4), "invalid input string"

    numOfGooglers = int(data[0])
    numOfSurprisingTriplets = int(data[1])
    p = int(data[2])

    scoreTotals = []
    for i in range(3, len(data)):
      scoreTotals.append(int(data[i]))

    return ScoreCollection(numOfGooglers, numOfSurprisingTriplets, p, scoreTotals)

  def calculateActualScores(self):
    numOfSurprisingTriplets = self.numOfSurprisingTriplets
    self.actualScores = []

    for currScoreTotal in self.scoreTotals:
      score = Score(currScoreTotal)
      surprisingScore = score.surprisingScore()
  
      if (numOfSurprisingTriplets>0 and max(surprisingScore) == self.p):
        self.actualScores.append(surprisingScore)
        numOfSurprisingTriplets = numOfSurprisingTriplets - 1
      else:
        self.actualScores.append(score.regularScore())

  def calculateActualScores_rev(self):
    numOfSurprisingTriplets = self.numOfSurprisingTriplets
    self.actualScores = []

    self.scoreTotals.reverse()

    for currScoreTotal in self.scoreTotals:
      score = Score(currScoreTotal)
      surprisingScore = score.surprisingScore()
  
      if (numOfSurprisingTriplets>0 and max(surprisingScore) == self.p):
        self.actualScores.append(surprisingScore)
        numOfSurprisingTriplets = numOfSurprisingTriplets - 1
      else:
        self.actualScores.append(score.regularScore())


  def _y(self):
    y = 0

    for score in self.actualScores:
      if (max(score) >= self.p):
        y = y + 1

    return y

  def y(self):
    self.calculateActualScores()
    y1 = self._y()
    self.calculateActualScores_rev()
    y2 = self._y()

    if (y1 > y2):
      return y1

    return y2



def readFromStdin():
  data = sys.stdin.readlines()

  return data

def readFromFile(filename):
  f = open(filename)
  data = f.readlines()
  f.close()
  
  return data

def main():
  if len(sys.argv) >= 2 and sys.argv[1] != '-':
    data = readFromFile(sys.argv[1])
  else:
    data = readFromStdin()

  numOfTestCases = int(data[0])

  assert (numOfTestCases == len(data)-1), "invalid data file"

  for i in range(1, len(data)):
    line = data[i]
    scoreCollection = ScoreCollection.makeFromInputStr(line)

    print "Case #%d: %d" % (i, scoreCollection.y())
    # print scoreCollection.actualScores

if __name__=="__main__":
  main()

