'''
Created on Mar 24, 2012

@author: fady
'''
f=open('B-large.in','r')
outputfile=open('out','w')
numberOfEntries=int(f.readline())
#==================
counter=0
while (counter<int(numberOfEntries)):
    counter=counter+1
    #===========================================
    line = f.readline()
    seperated=line.split()
    numberOfDancers=int(seperated[0])
    surprising=int(seperated[1])
    bestResultOf=int(seperated[2])
    lowestSure=(bestResultOf-1)*3+1
    highestSureNot=(bestResultOf-1)*3-2
    innerCounter=0
    dancersResults=[]
    sureDancers=[]
    while(innerCounter<numberOfDancers):
        dancersResults.append(int(seperated[innerCounter+3]))
        innerCounter=innerCounter+1
        unCertain=0
        certain=0
    for x in dancersResults:
        if (x==0):
            pass
        elif (x>=lowestSure):
            certain+=1
            
        elif (x>highestSureNot):
            unCertain+=1    
    if(bestResultOf==0):
        outputfile.write("Case #"+str(counter)+": "+str(numberOfDancers))
    elif(unCertain>surprising):
        outputfile.write("Case #"+str(counter)+": "+str(certain+surprising))
    else:
        outputfile.write("Case #"+str(counter)+": "+str(certain+unCertain))
    outputfile.write("\n")

