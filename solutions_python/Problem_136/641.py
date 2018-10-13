import time
import math

startTime = time.time()
FILENAME = "C:/Users/DENZEL CHUNG/Desktop/B-large.in"
#FILENAME = "C:/Users/DENZEL CHUNG/Desktop/cookieclicker.txt"
read = open(FILENAME, 'r')
inputs = read.read().split("\n") #split by new line
output = file("C:/Users/DENZEL CHUNG/Desktop/cookieclickerlargeoutput.txt", "w+")
idx = 0

#######################################
####################################### 
#test input
#trials = raw_input()
trials = inputs[idx]
idx += 1

for trialNum in range(int(trials)):
    
    cfx = inputs[idx]
    idx += 1
    #cfx = raw_input()
    c, f, x = cfx.split()
    
    # convert from str to float
    # c = cookie farm cost
    # f = cookie farm additional / sec
    # x = win
    c = float(c)
    f = float(f)
    x = float(x)
    
    totalTime = 0.0
    totalCookies = 0.0
    prevCookiesPerSec = cookiesPerSec = 2.0
    
    while totalCookies < x:
        testNextCookies = cookiesPerSec + f
        
        if (x / cookiesPerSec) - (c / cookiesPerSec) < (x / testNextCookies):
            totalTime += x / cookiesPerSec
            totalCookies += cookiesPerSec * (x / cookiesPerSec)
            break
        else:
            totalTime += c / cookiesPerSec
            cookiesPerSec += f
    print "Case #%d: %.7f" % (trialNum+1, totalTime)
    output.write("Case #%d: %.7f \n" % (trialNum+1, totalTime))
    
                
    #if len(match) == 1:
    #    print "Case #%d: %s" % (trialNum+1, match[0])
    #    output.write("Case #%d: %s \n" % (trialNum+1, match[0]))
    #elif len(match) > 1:
    #    print "Case #%d: %s" % (trialNum+1, "Bad magician!")
    #    output.write("Case #%d: %s \n" % (trialNum+1, "Bad magician!"))
    #else:
    #    print "Case #%d: %s" % (trialNum+1, "Volunteer cheated!")
    #    output.write("Case #%d: %s \n" % (trialNum+1, "Volunteer cheated!"))
        
#output.write("Case #%d: %d %d" % (trialNum+1, a+1, b+1))
            
#######################################
#######################################  
read.close()
output.close()


endTime = time.time()
print "Time Taken: %s" % (endTime-startTime)