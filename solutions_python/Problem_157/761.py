#!/usr/bin/env python

import fileinput

quaternions = {
      '1' :
         {
            '1' : '1',
            'i' : 'i',
            'j' : 'j',
            'k' : 'k'
         },
      'i' :
         {
            '1' : 'i',
            'i' : '-1',
            'j' : 'k',
            'k' : '-j'
         },
      'j' :
         {
            '1' : 'j',
            'i' : '-k',
            'j' : '-1',
            'k' : 'i'
         },
      'k' :
         {
            '1' : 'k',
            'i' : 'j',
            'j' : '-i',
            'k' : '-1'
         }
}

def getValueFromQuaternions(char1, char2):
   sign = 1

   if char1[0] == '-':
      sign ^= 1
      char1 = char1[1:]

   if char2[0] == '-':
      sign ^= 1
      char2 = char2[1:]

   value = quaternions[char1][char2]
   if sign == 0:
      if value[0] == '-':
         value = value[1:]
      else:
         value = '-' + value

   return value

def lookupTableSet(lookupTable, i, j, value):
   if i not in lookupTable:
      lookupTable[i] = {}
   lookupTable[i][j] = value

def lookupTableGet(lookupTable, i, j):
   if i not in lookupTable:
      return None
   if j not in lookupTable[i]:
      return None
   return lookupTable[i][j]

def canBeReducedToStr(testcase, str):
   if testcase == str:
      return True
   if len(testcase) < len(str):
      return False

   c = "1"

   if str == "ijk":
      for k in testcase:
         c = getValueFromQuaternions(c, k)
      if c != "-1":
         return False
   elif str == "jk":
      for k in testcase:
         c = getValueFromQuaternions(c, k)
      if c != "i":
         return False

   c = "1"

   for i in xrange(len(testcase) - len(str) + 1):
      c = getValueFromQuaternions(c, testcase[i])

      if c == str[0]:
         if len(str) > 1:
            if canBeReducedToStr(testcase[i+1:], str[1:]):
               return True
         else:
            return True

   return False

def canBeReduced(testcase):
   c = "1"
   for k in testcase:
      c = getValueFromQuaternions(c, k)
   if c != "-1":
      return False

   return canBeReducedToStr(testcase, "ijk")

if __name__ == "__main__":
   lineCount = 0
   testcaseCount = 0
   testcases = []
   repetition = 0

   for line in fileinput.input():
      if lineCount == 0:
         testcases = int(line) * [None]
         lineCount += 1
      else:
         if (lineCount & 1) == 0:
            testcases[testcaseCount] = repetition*line.strip()
            testcaseCount += 1
         else:
            repetition = int(line.split()[1])

         lineCount += 1

   testcaseCount = 0

   for testcase in testcases:
      testcaseCount += 1
      print ("Case #%ld: %s" % (testcaseCount, "YES" if canBeReduced(testcase) else "NO"))
