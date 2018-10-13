#!/usr/pubsw/bin/python
import sys

def processExample(lines, case_num):
    count = 0;
    for line in lines:
        count += line.count('#')
    if count % 4 != 0:
        printFail(case_num)
        return
    elif count == 0:
        printSuccess(lines, case_num)
        return
        
    linelen = len(lines[0])
    numlines = len(lines[:-1])
    #print('numlines: ' + str(numlines))
    #print('\n'.join(lines))
    #print('------')
    for i in range(numlines):
        #print("i is: " + str(i))
        firstPos = lines[i].find('#')
        while firstPos >= 0:
            if (firstPos+1) == linelen or lines[i][firstPos+1] != '#' or lines[i+1][firstPos:(firstPos+2)] != '##':
                printFail(case_num)
                return
            lines[i] = lines[i][:firstPos] + '/\\' + lines[i][(firstPos+2):]
            lines[i+1] = lines[i+1][:firstPos] + '\\/' + lines[i+1][(firstPos+2):]
            #print("I THINK")
            #print('\n'.join(lines[i:(i+2)]))
            firstPos = lines[i].find('#')
    if lines[-1].find('#') > 0:
        printFail(case_num)
    printSuccess(lines,case_num)

def printFail(case_num):
    print("Case #" + str(case_num) + ":\nImpossible")

def printSuccess(lines,case_num):
    print("Case #" + str(case_num) + ":")
    print('\n'.join(lines))

f = open(sys.argv[1])
all = f.readlines()

lineNum = 1
startLn = 0
endLn = 0
caseNum = 1;
while lineNum < len(all):
    if all[lineNum][0] == '.' or all[lineNum][0] == '#':
        startLn = lineNum
        all[lineNum] = all[lineNum][:-1]
        lineNum += 1
        while lineNum < len(all) and (all[lineNum][0] == '.' or all[lineNum][0] == '#'):
            all[lineNum] = all[lineNum][:-1]
            lineNum += 1
        endLn = lineNum
        processExample(all[startLn:endLn], caseNum)
        caseNum += 1
    lineNum += 1
        
