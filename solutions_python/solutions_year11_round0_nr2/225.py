#!/usr/bin/python

f = open("input.txt")
items = int(f.readline())
counter = 0

while counter < items:
     input = f.readline().strip().split(" ")
     combineDict = {}
     for x in range(0,int(input.pop(0))):
          startPhrase = input.pop(0)
          combineDict[startPhrase[0:2]] = startPhrase[2]
          temp = list(startPhrase)
          temp.reverse()
          startPhrase = "".join(temp)
          combineDict[startPhrase[1:3]] = startPhrase[0]
     exclusions = ""
     for x in range(0,int(input.pop(0))):
          exclusions += input.pop(0)
     ignoreMe = input.pop(0) # The way I am coding this, I don't need that int
     input = input.pop(0)
     finalList = ""
     for x in input:
          finalList += x
          if len(finalList) < 2:
               continue
          if len(combineDict) != 0:
               if combineDict.has_key(finalList[-2:]):
                    finalList = finalList.replace(finalList[-2:],combineDict[finalList[-2:]])
          if len(exclusions) != 0:
               y = exclusions.find(finalList[-1])
               if y != -1:
                    if y%2 == 0:
                         y = finalList.find(exclusions[y+1])
                    else:
                         y = finalList.find(exclusions[y-1])
                    if y != -1:
                         finalList = ""
     print "Case #"+str(counter+1)+": "+str(list(finalList)).replace("'","")
     counter+=1

f.close()