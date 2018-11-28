import time
import math
import random

def deceitful():
    global kenBlocks, naomiBlocks, kenDeceitfulWin, naomiDeceitfulWin
    
    maxStrKen = max(kenBlocks)
    maxKen = float(maxStrKen)
    #toldKen = maxKen - 0.00001
    
    if float(max(naomiBlocks)) > maxKen:
        chosenStrNaomi = max(naomiBlocks)
        chosenNaomi = float(chosenStrNaomi)
    else:
        chosenStrNaomi = min(naomiBlocks)
        chosenNaomi = float(chosenStrNaomi)
    chosenKen = maxKen
    
    kenBlocks.remove(maxStrKen)
    naomiBlocks.remove(chosenStrNaomi)
    
    if chosenKen > chosenNaomi:
        kenDeceitfulWin += 1
    else:
        naomiDeceitfulWin += 1


def normal():
    global kenBlocks2, naomiBlocks2, kenNormalWin, naomiNormalWin
    
    chosenStrNaomi = random.choice(naomiBlocks2)
    chosenNaomi = float(chosenStrNaomi)
    kenChoices = [block for block in kenBlocks2 if float(block) > chosenNaomi]
    if kenChoices:
        chosenStrKen = min(kenChoices)
        chosenKen = float(chosenStrKen)
    else:
        chosenStrKen = min(kenBlocks2)
        chosenKen = min([float(block) for block in kenBlocks2])
        
    kenBlocks2.remove(chosenStrKen)
    naomiBlocks2.remove(chosenStrNaomi)
    if chosenKen > chosenNaomi:
        kenNormalWin += 1
    else:
        naomiNormalWin += 1
        

startTime = time.time()
FILENAME = "C:/Users/DENZEL CHUNG/Desktop/Google Code Jam/D. Deceitful War/D-large.in"
#FILENAME = "C:/Users/DENZEL CHUNG/Desktop/Google Code Jam/D. Deceitful War/deceitfulwar.txt"
read = open(FILENAME, 'r')
inputs = read.read().split("\n") #split by new line
output = file("C:/Users/DENZEL CHUNG/Desktop/Google Code Jam/D. Deceitful War/largeoutput.txt", "w+")
idx = 0

#######################################
####################################### 
#test input
#trials = raw_input()
trials = inputs[idx]
idx += 1

for trialNum in range(int(trials)):
    
    numBlocks = int(inputs[idx])
    idx += 1
    naomiBlocks = inputs[idx].split()
    idx += 1
    kenBlocks = inputs[idx].split()
    idx += 1
    
    #numBlocks = int(raw_input())
    #naomiBlocks = raw_input().split()
    #kenBlocks = raw_input().split()
    naomiBlocks2 = list(naomiBlocks)
    kenBlocks2 = list(kenBlocks)

    
    kenDeceitfulWin = 0
    naomiDeceitfulWin = 0
    
    kenNormalWin = 0
    naomiNormalWin = 0
    
    for i in range(numBlocks):
        deceitful()
        
    for i in range(numBlocks):
        normal()
    
    print naomiDeceitfulWin, naomiNormalWin
    

    print "Case #%d: %d %d" % (trialNum+1, naomiDeceitfulWin, naomiNormalWin)
    output.write("Case #%d: %d %d \n" % (trialNum+1, naomiDeceitfulWin, naomiNormalWin))
    
       
            
#######################################
#######################################  
read.close()
output.close()


endTime = time.time()
print "Time Taken: %s" % (endTime-startTime)
