#!/usr/bin/python3

import sys

def playNormal(NaomiBlocks, KenBlocks):
  NaomiBlocks.sort()
  NaomiBlocks.reverse()
  KenBlocks.sort()
  counter = 0
  while NaomiBlocks:
    nVal = NaomiBlocks.pop()
    maxKen = 0
    for i in KenBlocks:
      if i > nVal:
        maxKen = i
        break

    if maxKen > nVal:
      KenBlocks.remove(maxKen)
    else:
      KenBlocks.remove(min(KenBlocks))
      counter += 1

  return counter


def playUnfaith(NaomiBlocks, KenBlocks):
  NaomiBlocks.sort()
  NaomiBlocks.reverse()
  KenBlocks.sort()

 # while NaomiBlocks:
  counter = 0
    #plays every loser blocks
  while NaomiBlocks:
    minNao = min(NaomiBlocks)
    minKen = min(KenBlocks)
    if (minKen > minNao):
      minKen = max(KenBlocks)
    else:
      counter += 1

    NaomiBlocks.remove(minNao)
    KenBlocks.remove(minKen)

  return counter


def parse(filename):
  f = open(filename)
  numTestCases = int(f.readline())
  numtestmax = numTestCases + 1
  while numTestCases:
    print ("Case #" + str(numtestmax - numTestCases) + ": ", end='')
    numBlocks =  int (f.readline())
    NaomiBlocks = [float(x) for x in f.readline().strip().split(" ")]
    KenBlocks = [float(x) for x in f.readline().strip().split(" ")]
    NaomiBlocks2 = NaomiBlocks[:]
    KenBlocks2 = KenBlocks[:]
    MaxNaomiNormal = playNormal(NaomiBlocks, KenBlocks)
    MaxNaomiCheat = playUnfaith(NaomiBlocks2, KenBlocks2)
    print (str(MaxNaomiCheat) + " " + str(MaxNaomiNormal))
#dec numTestCases
    numTestCases -= 1


def main():
  parse(sys.argv[1])

main()
