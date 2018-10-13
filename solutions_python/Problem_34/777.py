import sys
import re

nums = sys.stdin.readline()
[lword, ldict, lcases] = nums.split(' ')

dict1 = []
lines = sys.stdin.readlines()
for i in range(0,int(ldict)):
    dict1.append(lines[i][0:-1])

testcases = []
for i in range(int(ldict), len(lines)):
    testcases.append(lines[i][0:-1])

rxps = []
for case in testcases:
    if case.find('(') != -1:
        case = case.replace('(', '[')
        case = case.replace(')', ']')
    rxps.append(re.compile(case))

tc = 1
fil = open('out.txt', 'w')
for rxp in rxps:
    count = 0
    for i in dict1:
        if rxp.match(i):
              count = count + 1
    print 'Case #%d: %d' % (tc, count)
    fil.write('Case #'+str(tc)+': '+str(count)+'\n')
    tc = tc + 1
fil.close()
