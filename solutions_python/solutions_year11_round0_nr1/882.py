#!/usr/bin/env python

import os, numpy, math, sys

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])

output = ''

for t in range(T):
  line=lines[1+t].split()
  N = int(line[0])
  
  pathSign = []
  pathNumber = []
  pathStepDone = 0
  curO = 1
  curB = 1
  targetO = 1
  targetB = 1
  
  findNextTargetO = True
  findNextTargetB = True
  #Load paths
  for i in range(N):
    pathSign += str(line[1+i*2])
    pathNumber.append(str(line[2+i*2]))
  
  z = 0
  
  while (pathStepDone<N):
    #Find next target
    i = pathStepDone
    while ((i<N) and (findNextTargetO or findNextTargetB)):
      if (pathSign[i]=='O' and findNextTargetO):
        targetO = int(pathNumber[i])
        findNextTargetO = False
      if (pathSign[i]=='B' and findNextTargetB):
        targetB = int(pathNumber[i])
        findNextTargetB = False
      i+=1
    
    #print "OC %d; OT %d" %(curO, targetO)
    #print "BC %d; BT %d" %(curB, targetB)
    #print pathSign[pathStepDone]
    #print pathNumber[pathStepDone]
    
    robOhasDone = False
    robBhasDone = False
    targetDone = False
    
    #Pushed the button
    if (pathSign[pathStepDone] == 'O' and curO == targetO and robOhasDone == False):
      robOhasDone = True
      targetDone = True
      findNextTargetO = True
      #print "Push O button"
    elif (pathSign[pathStepDone] == 'B' and curB == targetB and robBhasDone == False):
      robBhasDone = True
      targetDone = True
      findNextTargetB = True
      #print "Push B button"
    
    #Move robots
    if (robOhasDone == False and targetO > curO):
      curO += 1
      #print "Move O"
    
    if (robOhasDone == False and targetO < curO):
      curO -= 1
      #print "Move O"
    
    if (robBhasDone == False and targetB > curB):
      curB += 1
      #print "Move B"
    
    if (robBhasDone == False and targetB < curB):
      curB -= 1
      #print "Move B"
    
    if (targetDone):
      pathStepDone+=1
    
    z+=1
  output += 'Case #%d: %d\n' % (t+1, z)

print output
file(sys.argv[1]+'.res','w').write(output)

