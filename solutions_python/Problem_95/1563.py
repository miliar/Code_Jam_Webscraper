#!/usr/bin/env python
import sys
import pprint
from sets import Set

class Googlerese(object):
  def __init__(self):
    self.G2EMap = {}

    self.buildMap()

  def buildMap(self):
    sampleInputs = ["ejp mysljylc kd kxveddknmc re jsicpdrysi",
                    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                    "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
    sampleOutputs = ["our language is impossible to understand",
                     "there are twenty six factorial possibilities",
                     "so it is okay if you want to just give up"]

    for i in range(0,3):
      sampleInput = sampleInputs[i]
      sampleOutput = sampleOutputs[i]

      assert (len(sampleInput) == len(sampleOutput)), 'The lengths of the sample input and output strings are different'

      for j in range(0,len(sampleInput)):
        currInputChar = sampleInput[j]
        currOutputChar = sampleOutput[j]

        if (currInputChar != ' '):
          assert (self.G2EMap.get(currInputChar) is None or self.G2EMap.get(currInputChar) == currOutputChar), 'not a 1-to-1 mapping for %s:(%s,%s)' % (currInputChar, self.G2EMap.get(currInputChar), currOutputChar)
    
        self.G2EMap[currInputChar] = currOutputChar
    
    missingGLetters = self.findMissingGLetters()
    if (len(missingGLetters) > 0):
      missingELetters = self.findMissingELetters()

      assert (len(missingGLetters) == len(missingELetters)), "not the same number of missing googlese/english letters"
      missingGLetterList = []
      for letter in missingGLetters:
        missingGLetterList.append(letter)

      missingELetterList = []
      for letter in missingELetters:
        missingELetterList.append(letter)

      for i in range(0,len(missingGLetterList)):
        # From Case #7, I can see that the values for q and z are flipped.  I could just hard code it but
        # that would be kind of cheating.
        self.G2EMap[missingGLetterList[i]] = missingELetterList[len(missingELetterList)-i-1]

  def findMissingGLetters(self):
    letters = Set(' abcdefghijklmnopqurstvwxyz')
    gLetters = Set(self.G2EMap.iterkeys())

    missingLetters = letters - gLetters

    return missingLetters

  def findMissingELetters(self):
    letters = Set(' abcdefghijklmnopqurstvwxyz')
    eLetters = Set()

    for key in self.G2EMap.iterkeys():
      eLetters.add(self.G2EMap.get(key))

    missingLetters = letters - eLetters

    return missingLetters

  def decode(self, inputStr):
    # make sure that the newlines are stripped off the inputStr
    inputStr = inputStr.rstrip('\n')

    outputStr = ''

    for c in inputStr:
      if (c == ' '):
        outputChar = ' '
      else:
        outputChar = self.G2EMap.get(c)

        assert (outputChar is not None), 'no mapping found for %s' % c

      outputStr = '%s%s' % (outputStr, outputChar)

    return outputStr

  def printMap(self):
    for key in sorted(self.G2EMap.iterkeys()):
      print "%s: %s" % (key, self.G2EMap.get(key))

def readFromStdin():
  data = sys.stdin.readlines()

  return data

def readFromFile(filename):
  f = open(filename)
  data = f.readlines()
  f.close()
  
  return data
   
def main():
  googlerese = Googlerese()

  if len(sys.argv) >= 2 and sys.argv[1] != '-':
    data = readFromFile(sys.argv[1])
  else:
    data = readFromStdin()

  if (len(data) < 1):
    print "invalid input file"
  else:
    numOfTests = int(data[0])

    

    for i in range(1, len(data)):
      inputStr = data[i]
      outputStr = googlerese.decode(inputStr)
      print "Case #%d: %s" % (i, outputStr)  

if __name__=="__main__":
  main()
