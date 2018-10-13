#!/usr/bin/python

f = open("input.txt")
items = int(f.readline())
counter = 0

while counter < items:
     bleh = f.readline()
     input = []
     for x in f.readline().strip().split(" "):
          input.append(int(x))
     sortedArray = list(input)
     sortedArray.sort()
     notRight = 0
     for x in range(0,len(sortedArray)):
          if sortedArray[x] != input[x]:
               notRight += 1
     print "Case #"+str(counter+1)+": "+str(notRight)+".000000"
     counter+=1

f.close()