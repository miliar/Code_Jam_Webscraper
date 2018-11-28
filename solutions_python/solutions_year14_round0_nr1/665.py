import time
import math

startTime = time.time()
FILENAME = "C:/Users/DENZEL CHUNG/Desktop/A-small-attempt0.in"
#FILENAME = "C:/Users/DENZEL CHUNG/Desktop/magician.txt"
read = open(FILENAME, 'r')
inputs = read.read().split("\n") #split by new line
output = file("C:/Users/DENZEL CHUNG/Desktop/output.txt", "w+")
idx = 0

#######################################
####################################### 
#test input
#trials = raw_input()
trials = inputs[idx]
idx += 1

for trialNum in range(int(trials)):
    firstArrangement = list()
    secondArrangement = list()
    match = list()
    
    #firstAnswer = int(raw_input())
    firstAnswer = int(inputs[idx])
    idx += 1
    
    for i in range(4):
        #arrangement = raw_input()
        arrangement = inputs[idx]
        idx += 1
        firstArrangement.append(arrangement.split())
        
    #secondAnswer = int(raw_input())
    secondAnswer = int(inputs[idx])
    idx += 1
    for i in range(4):
        #arrangement = raw_input()
        arrangement = inputs[idx]
        idx += 1
        secondArrangement.append(arrangement.split())
    
    for first in firstArrangement[firstAnswer-1]:
        for second in secondArrangement[secondAnswer-1]:
            if first == second:
                match.append(first)
                
    if len(match) == 1:
        print "Case #%d: %s" % (trialNum+1, match[0])
        output.write("Case #%d: %s \n" % (trialNum+1, match[0]))
    elif len(match) > 1:
        print "Case #%d: %s" % (trialNum+1, "Bad magician!")
        output.write("Case #%d: %s \n" % (trialNum+1, "Bad magician!"))
    else:
        print "Case #%d: %s" % (trialNum+1, "Volunteer cheated!")
        output.write("Case #%d: %s \n" % (trialNum+1, "Volunteer cheated!"))
        
#output.write("Case #%d: %d %d" % (trialNum+1, a+1, b+1))
            
#######################################
#######################################  
read.close()
output.close()


endTime = time.time()
print "Time Taken: %s" % (endTime-startTime)