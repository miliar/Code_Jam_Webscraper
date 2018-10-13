f = open('A-small-practice.in', 'r')
g = open('output.txt', 'w')

NUM_OF_ROWS = 4
numTestCases = int(f.readline())

i = 0
while (i < numTestCases):
   rowNumberA = int(f.readline())
   j = 0
   while (j < NUM_OF_ROWS):
      if (j == rowNumberA - 1):
         rowOfCardsA = (map(int, (f.readline()).split()))
         rowSetA = set(rowOfCardsA)
      else:
         temp = f.readline()
      j = j + 1;

   rowNumberB = int(f.readline())
   j = 0
   while (j < NUM_OF_ROWS):
      if (j == rowNumberB - 1):
         rowOfCardsB = (map(int, (f.readline()).split()))
         rowSetB = set(rowOfCardsB)
      else:
         temp = f.readline()
      j = j + 1;
   
   setsCombined = rowSetA & rowSetB
   cardinality = len(setsCombined)
   
   if (cardinality == 1):
      g.write("Case #" + str(i+1) +": " + str(setsCombined.pop()) + "\n")
   elif (cardinality > 1):
      g.write("Case #" + str(i+1) +": " + "Bad magician!" + "\n")
   else:
      g.write("Case #" + str(i+1) +": " + "Volunteer cheated!" + "\n")
   i = i + 1
f.close()
g.close()
