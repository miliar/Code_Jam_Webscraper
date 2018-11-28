# cook your code here
import sys

noOfTestCases = 0
count = 0
testcases =[]

for line in sys.stdin:
    if count == 0 :
        noOfTestCases = line
    else :
        testcases.append(line)    
    count += 1
    
caseno = 1    
for testcase in testcases :
    case = testcase.split(" ")
    smax = int(case[0])
    sseq = case[1]
    index = 0
    digit = 1
    noofclappingppl = 0
    notointroduce = 0
    for s in range(0, smax+1) :
        si = int(sseq[index : index + digit])
        index += 1
        if si > 0 :
            if noofclappingppl >= s or s == 0 :
                noofclappingppl += si    
            else :
                needed = s-noofclappingppl
                noofclappingppl += si + needed
                notointroduce += needed
    print "Case #"+str(caseno)+":",notointroduce
    caseno += 1