from __future__ import division


FILE_NAME = 'B-large.in'

numCases = 0
testCases = []
with open(FILE_NAME,'r') as file:
    numCases = int(file.readline())
    for case in xrange(numCases):
        testCases.append([float(x) for x in file.readline().split()])
           

def c(farm_cost,farm_cps,goal):
    total_time = 0
    farm_count = 0
    farm_time = 0
    prev_farm_time = 0
    cps = 2
    while True:
##        print "Farm Count: {} Farm Time: {} cps: {} total_time {}".format(
##            farm_count,farm_time,cps,total_time)
        new_time = goal / cps + farm_time
        if new_time < total_time or total_time == 0:
            total_time = new_time
        elif new_time > total_time:
            return round(total_time,7)
        farm_count += 1
        prev_farm_time = farm_time
        farm_time = farm_cost / cps + prev_farm_time
        cps = 2 + farm_count * farm_cps
    
    

    
    

caseNum = 1
with open('results.txt','w') as file:
    for test in testCases:
        file.write('Case #{}: {}\n'.format(caseNum,c(test[0],test[1],test[2])))
        caseNum += 1
    

