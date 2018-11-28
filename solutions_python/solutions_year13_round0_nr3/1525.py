import math
import os
import sys
import math


def solvePbs(pbs,pathOut):
  fout = open(pathOut,'w')
  kb = buildKnowledgeBase(10000000)
  for i in range(len(pbs)):
    fout.write("Case #"+str(i+1)+": "+solveCase(pbs[i],kb)+'\n')
  fout.close()

def isPalindrome(number):
  end = len(number)-1
  for i in range(len(number)/2):
    if not number[i] == number[end]:
      return False
    else:
      end -= 1
  return True

def buildKnowledgeBase(maxi):
  nb = [0]
  for i in range(1,maxi+1):
    if isPalindrome(str(i)) and isPalindrome(str(i**2)):
      nb.append(nb[-1]+1)
    else:
      nb.append(nb[-1])
  return nb

def solveCase(pb,kb):
  mini = long(math.ceil(math.sqrt(pb[0])))
  maxi = long(math.sqrt(pb[1]))
  return str(kb[maxi]-kb[mini-1])

def readIntLine(line):
  elems = line.split(' ')
  toReturn = []
  for e in elems:
    toReturn.append(long(e))
  return toReturn

def readFloatLine(line):
  elems = line.split(' ')
  toReturn = []
  for e in elems:
    toReturn.append(float(e))
  return toReturn


def breakInCases(pathIn):
  cases = []
  fin = open(pathIn,'r')
  lines = fin.readlines()
  for line in lines[1:]:
    cases.append(readIntLine(line))
  return cases 
 
def main():
  args = sys.argv[1:]
  cases = breakInCases(args[0])
  solvePbs(cases,args[1])

if __name__ == "__main__":
  main()

# vim:set encoding=utf-8 
# vim:set fileencoding=utf-8

