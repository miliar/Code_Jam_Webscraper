#!/usr/bin/python

f = open("input.txt")
items = int(f.readline())
counter = 0

while counter < items:
     lastAction = ""
     orangePos = 1
     bluePos = 1
     timeDiff = 0
     totalTime = 0
     input = f.readline().strip().split(" ")
     buttonPresses = int(input.pop(0))
     for x in range(0, buttonPresses):
          tempDiff = 0
          if input[x*2] == "O":
               tempDiff = abs(orangePos-int(input[(x*2)+1]))+1
               orangePos = int(input[(x*2)+1])
               if lastAction != "O":
                    tempDiff -= timeDiff
                    if tempDiff < 1:
                         tempDiff = 1
                    timeDiff = tempDiff
               else:
                    timeDiff += tempDiff
          if input[x*2] == "B":
               tempDiff = abs(bluePos-int(input[(x*2)+1]))+1
               bluePos = int(input[(x*2)+1])
               if lastAction != "B":
                    tempDiff -= timeDiff
                    if tempDiff < 1:
                         tempDiff = 1
                    timeDiff = tempDiff
               else:
                    timeDiff += tempDiff
          totalTime+=tempDiff
          lastAction = input[x*2]
     print "Case #"+str(counter+1)+": "+str(totalTime)
     counter+=1
