import sys, copy

def parseInputFile(inputFile):
   case = 1
   with open(inputFile, 'r') as file:
      tests = int(file.readline())
      while tests > 0:
         tests -= 1
         value = file.readline().strip()
         valueList = list(value)

         if value:
            print("Case #{0}: {1}".format(case, findHighestTidyValue(value)))
            case += 1

def findHighestTidyValue(value):
   while not isTidy(value):
      value = subtract(value)
      # print(value)
   return value

def subtract(value):
   valueList = list(value)
   # Find next non-tidy digit and subtract 1 from it
   i = 0
   for i in range(1, len(valueList)):
      if valueList[i] < valueList[i-1]:
         valueList[i-1] = str(int(valueList[i-1])-1)
         while i < len(valueList):
            valueList[i] = '9'
            i += 1
   # Trim leading 0s
   for i in range(0, len(valueList)):
      if valueList[i] != '0':
         valueList = valueList[i:]
         break
   # print(valueList)
   return ''.join(valueList)

def isTidy(value):
   valueList = list(value)
   return sorted(valueList) == valueList

def main(argv):
   parseInputFile(argv[1])

main(sys.argv)
