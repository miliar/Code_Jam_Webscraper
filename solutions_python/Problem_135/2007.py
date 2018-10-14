import sys

dataSetCount = int(sys.stdin.readline().strip())

for i in range(dataSetCount):
   firstAnswer = int(sys.stdin.readline())

   rows1 = []
   rows1.append(sys.stdin.readline().strip().split())
   rows1.append(sys.stdin.readline().strip().split())
   rows1.append(sys.stdin.readline().strip().split())
   rows1.append(sys.stdin.readline().strip().split())
   secondAnswer = int(sys.stdin.readline())

   rows2 = []
   rows2.append(sys.stdin.readline().strip().split())
   rows2.append(sys.stdin.readline().strip().split())
   rows2.append(sys.stdin.readline().strip().split())
   rows2.append(sys.stdin.readline().strip().split())

   matchingSet = set(rows1[int(firstAnswer)-1]) & set(rows2[int(secondAnswer)-1])

   if len(matchingSet) == 1:
      for match in matchingSet:
         print 'Case #' + str(i + 1) + ': ' + match
   elif len(matchingSet) == 0:
      print 'Case #' + str(i + 1) + ': Volunteer cheated!'
   elif len(matchingSet) > 1:
      print 'Case #' + str(i + 1) + ': Bad magician!'

