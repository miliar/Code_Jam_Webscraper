import math

inputFile = open("probOneIn.txt", "r")
outputFile = open("probOneOut.txt", "w")
testCases = int(inputFile.readline())
for i in range(testCases):
   totalPancakes, neededPancakes = [int(x) for x in inputFile.readline().split()]
   pancakes = []
   sideArea = []
   for j in range(totalPancakes):
      newPancake = [int(x) for x in inputFile.readline().split()]
      pancakes.append(newPancake)
      sideArea.append(2 * math.pi * newPancake[0] * newPancake[1])
   bestAnswer = 0
   if i == 0:
      print(pancakes)
      print(sideArea)
      print("\n")
   pancakes = [x[0] for x in sorted(zip(pancakes, sideArea), key = lambda l: l[1], reverse = True)]
   sideArea.sort(reverse = True)
   if i == 0:
      print(pancakes)
      print(sideArea)
      print("\n")
   for j in range(len(pancakes)):
      answer = math.pi * pancakes[j][0] * pancakes[j][0] + 2 * math.pi * pancakes[j][0] * pancakes[j][1]
      pancakesTemp = pancakes[:j] + pancakes[j + 1:]
      sideAreaTemp = sideArea[:j] + sideArea[j + 1:]
      taken = 1
      if i == 0: print(j)
      if neededPancakes > 1:
         for k in range(totalPancakes - 1):
            if pancakesTemp[k][0] > pancakes[j][0]:
               if i == 0: print("continuing from " + str(k))
               if i == 0: print(str(k) + " " + str(pancakes[j][0]))
               continue
            answer += sideAreaTemp[k]
            taken += 1
            if i == 0: print(k)
            if taken == neededPancakes:
               break
         if taken < neededPancakes:
            if i == 0: print("not enough found")
            continue
      if i == 0: print(answer)
      if answer > bestAnswer:
         bestAnswer = answer
      if i == 0: print("\n")
   if(i < testCases - 1):
      outputFile.write("Case #" + str(i + 1) + ": " + str(bestAnswer) + "\n")
   else:
      outputFile.write("Case #" + str(i + 1) + ": " + str(bestAnswer))