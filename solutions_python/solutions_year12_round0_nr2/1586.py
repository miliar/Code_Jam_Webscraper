#! /usr/local/bin/python
import sys
import string

def openFile(fileName):
    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()
    return lines

def formatLines(lines):
    y = 0
    while y < len(lines):
        lines[y] = lines[y].rstrip('\n')
        y +=1
    return lines
   
googEng={'y':'a','e':'o', 'q':'z'}

fileNameInput = '/Users/erynmaynard/Desktop/GoogleCodeJam/Problem2/B-large.in'
inputLines = openFile(fileNameInput)
inputLines = formatLines(inputLines)
inputLines = inputLines[1:]

fileNameOutput = '/Users/erynmaynard/Desktop/GoogleCodeJam/Problem2/finalOutput.in'
output = open(fileNameOutput, 'w')


#inputLines = inputLines[1:3]

print(inputLines)
q=1
for x in inputLines:
    case = x.split(' ')
    surprising = int(case[1])
    p = int(case[2])
    tp = case[3:]
    total = 0
    for y in tp:
        y = int(y)
        for z in [0,1, 2, 3, 4]:
            if z ==0:
                if y%3 == 0 and y/3>=p:
                    total += 1
                    break
            if z > 0 and z < 3:
                if (y-z)%3 == 0 and (y-z)/3+1>=p:
                    total += 1
                    break
            if z >= 3:
                if surprising > 0 and y>0 and (y-z+1)%3 == 0 and (y-z+1)/3+2>=p:
                    total += 1
                    surprising -= 1
                    break
    print('Case #'+ str(q) +': ' + str(total))
    output.write('Case #'+ str(q) +': ' + str(total) + '\n')
    q +=1
output.close()
