'''
Created on 12.04.2014

@author: Johann
'''
def revenue(x):
    if x<0:
        x=0
    return 2+x*farmProfit

with open("input.txt", "rb") as aFile:
    with open("output.txt","wb") as outFile:
        testCases=int(aFile.readline())
        #print testCases
        for case in xrange(testCases):
            farmCost,farmProfit,goal=map(float,aFile.readline().split())
            #print farmCost,farmProfit,goal
            time=0
            if goal>farmCost:
                timeToGoal=goal/revenue(0)
                lastTimeToGoal=timeToGoal+1
                i=0
                while(timeToGoal<=lastTimeToGoal):
                    lastTimeToGoal=timeToGoal
                #for i in xrange(int(goal/farmCost)-1):
                    timeToGoal=time+goal/revenue(i)
                    time+=farmCost/revenue(i)
                    i+=1
                time=lastTimeToGoal
            else:
                time+=goal/revenue(int(goal/farmCost)-1)
                      
            outFile.write('Case #%d: %0.7f\n'%(case+1,time))        
            print 'Case #%d: %0.7f'%(case+1,time)