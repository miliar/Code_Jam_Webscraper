linesArray = open("A-large.in", "r").read().split("\n")
output = open("output.txt", "w")
writeString = ""
trials = int(linesArray[0])
for x in range(1, trials+1):
   peopleNeeded = 0
   tempArray = linesArray[x].split(" ")
   crowdArray = tempArray[1]
   numPeople = int(crowdArray[0])
   for y in range(1, len(crowdArray)):
      if y > numPeople:
         peopleNeeded += y-numPeople
         numPeople += y-numPeople
      else:
         peopleNeeded += 0
      numPeople += int(crowdArray[y])
   if x != trials+1:
      writeString+="Case #"+str(x)+": "+str(peopleNeeded)+"\n"
   else:
      writeString+="Case #"+str(x)+": "+str(peopleNeeded)
output.write(writeString)