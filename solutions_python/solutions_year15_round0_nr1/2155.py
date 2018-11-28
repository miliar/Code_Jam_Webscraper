inputFilename = "A-large.in"
outputFilename = "A-large.out"
f = open(inputFilename, 'r')
g = open(outputFilename, 'w')
testCases = f.readline()

h = 0
for line in f:
   
   inputLine = map(str, line.split())
   maxShyness = int(inputLine[0])
   audience = inputLine[1]
   
   standingAudience = int(audience[0])
   friends = 0
   
   audienceLength = maxShyness + 1
   for x in xrange(1, audienceLength):
      if standingAudience + friends < x:
         difference = x - friends - standingAudience
         friends += difference
      standingAudience += int(audience[x])
   
   g.write("Case #" + str(h+1) + ": " + str(friends)+"\n")
   h += 1