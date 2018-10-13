def rotate (toRotate):
   restOfString = str(toRotate)[:-1]
   firstDigit = str(toRotate)[len(restOfString):]
   
   return int(firstDigit + restOfString)
   

def getPairs (pairsFrom):
   currPairs = []
   
   current = rotate(pairsFrom)
   
   i = 0
   while i < len(str(pairsFrom)):
      if pairsFrom != current and len(str(pairsFrom)) == len(str(current)):
         currPairs.append((pairsFrom, current))
      current = rotate(current)
      i += 1
   
   return currPairs

def numPairs (a, b):
   pairs = []
   
   i = a
   while i <= b:
      tempPairs = getPairs(i)
      
      for pair in tempPairs:
         first, second = pair
         if second >= a and second <= b and pairs.count(pair) == 0 and pairs.count((second, first)) == 0:
            pairs.append(pair)
            
      i += 1
   return len(pairs)

f = open("input.txt", "r");
lines = f.readlines()
f.close()

# Get the number of lines and shorten the array
numLines = int(lines[0].strip())
lines = lines[1:]

f = open("output.txt", "w");

i = 1
for line in lines:
   words = line.split(' ')
   f.write("Case #" + str(i) + ': ')
   f.write(str(numPairs(int(words[0]), int(words[1]))) + '\n')
   i += 1
	
f.close()