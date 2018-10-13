#!/usr/bin/python
import sys

if (len(sys.argv) != 2):
  print "Usage: python " + sys.argv[0] + " inputFilename"
  exit()

inputf = open(sys.argv[1], 'r')
outputf = open('output.txt', 'w')

T = int(inputf.readline())
MAX_ROWS = 4

for t in range(T):

    ans1 = int(inputf.readline())
    
    for i in range(MAX_ROWS):
        line = inputf.readline()
        if (i + 1 == ans1):
            line1 = line.split(' ')
            for j in range(MAX_ROWS):
                line1[j] = int(line1[j])
    
    ans2 = int(inputf.readline())
    
    for i in range(MAX_ROWS):
        line = inputf.readline()
        if (i + 1 == ans2):
            line2 = line.split(' ')
            for j in range(MAX_ROWS):
                line2[j] = int(line2[j])
    
    result = []
    
    for i in range(MAX_ROWS):
        for j in range(MAX_ROWS):
            if line1[i] == line2[j]:
                result.append(line1[i])
                
    
    outputf.write('Case #')
    outputf.write(str(t+1))
    outputf.write(': ')
    if len(result) == 0:
        outputf.write('Volunteer cheated!')
    elif len(result) == 1:
        outputf.write(str(result[0]))
    elif len(result) > 1:
        outputf.write('Bad magician!')
    outputf.write('\n')
    
