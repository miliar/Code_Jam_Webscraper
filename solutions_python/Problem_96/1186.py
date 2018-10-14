import sys

if (len(sys.argv) != 2):
  print "Require 1 input file as argument"
  exit(1)
  
inputFile = open(sys.argv[1])
outputFile = open("output.txt", 'w')
N = int(inputFile.readline())

for i in range(N):
  inputTXT = inputFile.readline()[:-1]
  outputTXT = ""
  
  # My code here...
  inputNums = map(int, inputTXT.split(' '))
  n = inputNums[0] # number of Googlers
  s = inputNums[1] # number of surprising triplets
  p = inputNums[2] # lowest best-score allowed
  scores = inputNums[3:3+n]
  
  count = 0
  for score in scores:
    scoreLeft = score - p
    if scoreLeft < 0:
      continue
    if (p-1)*2 <= scoreLeft:
      count += 1
    elif s > 0: # can be surprising
      if (p-2)*2 <= scoreLeft:
        count += 1
        works = False
        s -= 1
  outputTXT = str(count)

  outputFile.write("Case #%d: %s\n" % (i+1, outputTXT))
  print "Case #%d: %s" % (i+1, outputTXT)

inputFile.close()
outputFile.close()
