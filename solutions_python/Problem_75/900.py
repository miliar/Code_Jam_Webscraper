#!/usr/bin/env python

import os, numpy, math, sys

infile = open(sys.argv[1],"r")
lines = infile.readlines()
infile.close()

T=int(lines[0])

output = ''

for t in range(T):
  print '%d of %d' % (t+1, T)
  line=lines[1+t].split()
  C = int(line[0])
  combineElementsSource = []
  combineElementsChange = []
  opposedElements = []
  for i in range (C):
    combineElementsSource.append(line[(i + 1)][0:2])
    combineElementsChange.append(line[(i + 1)][2])
  
  D = int(line[1 + C])
  for i in range (D):
    opposedElements.append(line[2 + C + i])
  
  sourceWord = str(line[3 + C + D])
  
  resultWord = []
  for i in range(len(sourceWord)):
    resultWord.append(sourceWord[i])
    if (len(resultWord)>1):
      #change
      for z in range(C):
        if ((resultWord[len(resultWord)-1] == combineElementsSource[z][0] 
          and (resultWord[len(resultWord)-2]==combineElementsSource[z][1])) or
          (resultWord[len(resultWord)-1] == combineElementsSource[z][1] 
          and (resultWord[len(resultWord)-2]==combineElementsSource[z][0]))):
            resultWord.pop(len(resultWord)-1)
            resultWord[len(resultWord)-1] = combineElementsChange[z]
            break
      #opposed
      for z in range(D):
        for j in range (len(resultWord)):
          for k in range (j+1, len(resultWord)):
            if ((resultWord[j] == opposedElements[z][0] 
              and (resultWord[k]==opposedElements[z][1])) or
              (resultWord[j] == opposedElements[z][1] 
              and (resultWord[k]==opposedElements[z][0]))):
                resultWord=[]
                break
                
  
  output += 'Case #%d: [' % (t+1) 
  if (len(resultWord) > 0):
    for i in range(len(resultWord)-1):
      output +='%s, ' % (resultWord[i])
    output +='%s' % (resultWord[len(resultWord)-1])
  output += ']\n'

print output
file(sys.argv[1]+'.res','w').write(output)

