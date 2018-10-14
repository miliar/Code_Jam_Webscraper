import sys

fileName = sys.argv[1]

def main():
  with open(fileName) as FileReader:
    testCases = int(FileReader.readline())
    for caseIndex in range(1, testCases + 1):
      Smax, shyAudiences = FileReader.readline().split(" ")
      applauding_audience_count = shynessLevel = y = 0
      while shynessLevel <= int(Smax):
        if shynessLevel > applauding_audience_count + y:
          y += 1
          continue
        applauding_audience_count += int(shyAudiences[shynessLevel])
        shynessLevel += 1
      print "Case #" + str(caseIndex) + ": " + str(y)

main()