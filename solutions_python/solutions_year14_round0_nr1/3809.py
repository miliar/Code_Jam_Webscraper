import sys
inputFile = open('A-small-attempt3.in')
count = 0
testdata = {}
testcases = inputFile.readline()
testcase =0
row_number = 0
result = []
for line in inputFile:
    if count%5==0:
        testcase +=1
        row_number = int(line.strip())
    elif count%5==row_number:
        row = line.strip().split(' ');
        testdata[testcase]=row
        if testcase%2==0:
            result.append([data for data in testdata[testcase] if data in testdata[testcase-1]])
    count +=1
case = 1
outputfile = open('output.txt','w+')
print result
for value in result:
    outputfile.write("Case #"+str(case)+": ")
    if len(value) == 1:
        outputfile.write(value[0]+'\n')
    if len(value) >1:
        outputfile.write("Bad Magician!"+'\n')
    if len(value) == 0:
        outputfile.write("Volunteer Cheated!"+'\n')
    case +=1
