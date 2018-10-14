### Set the input and output file names
import time
import datetime
import string
import operator
from collections import defaultdict

filename = 'C-large'
input_filename = filename + '.in'
output_filename = filename + '.out.' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S') + '.txt'

def greatestPowerOfTwo(x):
    #returns integer N where N is maximal such that 2**N <= x

    for n in range(0,70):
        if 2**n > x:
            ret = n - 1
            break
    return ret

    
def oneMorePoos(myD):
    #returns modified dictionary

    biggestGap = sorted(myD, reverse=True)[0]
    
    #Reduce number of gaps for first tuples by 1, deleting if completely gone
    if myD[biggestGap] > 1:
        myD[biggestGap] = myD[biggestGap] - 1
    else: 
        del myD[biggestGap]
        
    #Add the new gaps created from the stall being filled
    if biggestGap == 2: #if gap is 2 big, create just one gap of size 1
        myD[1] += 1
    elif biggestGap % 2 == 0: #divisible by 2 (min of 4)
        myD[biggestGap/2] += 1
        myD[biggestGap/2 - 1] += 1
    elif biggestGap > 1: #not divisible by 2 (min value of 3)
        myD[(biggestGap - 1)/2] += 2
    #else: do nothing if the biggest gap was 1 big (no new gaps were created)
    
    return myD


def manyMorePoos(myD, people):
    #returns modified dictionary

    biggestGap = sorted(myD, reverse=True)[0]
    
    #Reduce number of gaps for first tuples by 1, deleting if completely gone
    if myD[biggestGap] > people:
        leftpeople = 0
        poopers = people
        myD[biggestGap] = myD[biggestGap] - people
    else:
        leftpeople = people - myD[biggestGap]
        poopers = myD[biggestGap]
        del myD[biggestGap]
        
    #Add the new gaps created from the stall being filled
    if biggestGap == 2: #if gap is 2 big, create just one gap of size 1
        myD[1] += poopers
    elif biggestGap % 2 == 0: #divisible by 2 (min of 4)
        myD[biggestGap/2] += poopers
        myD[biggestGap/2 - 1] += poopers
    elif biggestGap > 1: #not divisible by 2 (min value of 3)
        myD[(biggestGap - 1)/2] += 2 * poopers
    #else: do nothing if the biggest gap was 1 big (no new gaps were created)
    
    return (myD, leftpeople)
    
    
def MaxMinStalls(myD):
    #returns tuple of max and min choices available
    biggestGap = sorted(myD, reverse=True)[0]
    smallestGap = sorted(myD)[0]
    
    if biggestGap % 2 == 0: #divisible by 2
        myMax = biggestGap/2
    else:
        myMax = (biggestGap - 1)/2

    if smallestGap % 2 == 0: #divisible by 2
        myMin = biggestGap/2 - 1
    else:
        myMin = (biggestGap - 1)/2
        
    return (myMax, myMin)
    
    
# stallState = defaultdict(int)

# stallState.clear()
# stallState[10**6] += 1

# start_time = time.time()
# #TESTING OF SINGLE POO
# #i = 1
# # while i <= 10**6 - 1:
# #     oneMorePoos(stallState)
# #     #print(i+1, "  ", sorted(stallState.items()))
# #     i += 1

# i = 524286
# while i >=1:
    # stallState, i = manyMorePoos(stallState, i)
    # print(i, "  ", sorted(stallState.items()))
    
# print(stallState)
# print("--- %s seconds ---" % (time.time() - start_time))


### Open input file for reading
with open(input_filename) as f:
    lines = f.read().splitlines()

    ### Open output file for writing
    with open(output_filename, 'w') as output:

        ######################################################
        ### Initialise variables from first line of the file
        ######################################################   
        vars = lines[0].split(' ')
        cases = int(vars[0])                    # number of cases
        print(str(cases) + ' cases detected.')  # [soft validation]
        lineNum = 1                             # first case starts here
        caseNum = 0                             # for counting the num of cases
        caseSize_r = 1                          # number of rows in each case; default = 1
        caseSize_c = 1                          # number of columns in each case; default = 1
        
        #infoLines = True                        # Toggle according to question
        infoLines = False                       # Toggle according to question
        
        ### i.e. infoLines == True
        if infoLines:
            output.write('NA')
        ### i.e. infoLines == False
        else:
            start_time = time.time()
            
            stallState = defaultdict(int)
            for caseNum in range(1, cases+1):
                
                ### Do the Work!
                ### TODO! 
                # N = number of stalls (less 2)
                N = int(lines[lineNum].split(' ')[0])
                # K = number of people going to pee
                K = int(lines[lineNum].split(' ')[1])
                
                #initiate dictionary (k,v)
                #  k = size of gap (key) 
                #  v = number of these gaps left (value)
                #ASSUMPTION: the 'min' will be from the gap of minimum size, 
                #            and the 'max' will be from the gap of maximum size
                stallState.clear()
                stallState[N] += 1
                i = K-1
                while i >= 1:
                    stallState, i = manyMorePoos(stallState, i)
                #    print(i, "  ", stallState)
                
                biggestGap = sorted(stallState, reverse=True)[0]
                
                if biggestGap % 2 == 0: #divisible by 2
                    myAns1 = biggestGap/2
                    myAns2 = biggestGap/2 - 1
                else:
                    myAns1 = (biggestGap - 1)/2
                    myAns2 = (biggestGap - 1)/2
                
                #len(lines[lineNum])
                lineNum += 1
                
                ### Output myAns
                print('Case #%d: %d %d\n' % (caseNum, myAns1,  myAns2))
                output.write('Case #%d: %d %d\n' % (caseNum, myAns1,  myAns2))
                
            print("--- %s seconds ---" % (time.time() - start_time))
                

### END
