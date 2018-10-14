import os
import sys
from pprint import pprint



def main():
  filePtr = open("in.in",'r')
  fileLines = filePtr.readlines()
  fileLines = [x.rstrip('\n') for x in fileLines]
  filePtr.close()

  noOfTest = fileLines[0]

  for num in range (1, int(noOfTest)+1):
    inp = fileLines[num].split(" ")
    sMax = int(inp[0])
    order = inp[1]
    #pprint(order)
    i = 0
    total = 0
    diff = 0
    for sI in order:
      #print sI
      if i <= total:
        total = total + int(sI)
      elif int(sI):
        currentDiff = i - total
        total = total + currentDiff + int(sI)
        diff = diff + currentDiff
      i = i + 1
      #print "## ",total, diff,i-1
      
    sys.stdout.write("Case #")
    sys.stdout.write(str(num))
    print ":",diff




# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    main()
