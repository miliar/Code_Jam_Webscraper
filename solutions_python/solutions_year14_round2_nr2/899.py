inputFile = open('B-small-attempt0 (1).in', 'r')
file1 = inputFile


file2 = open("New_Lottery_Game_Solution.txt", 'w')
### Actual Function ###

def magicFunction (file1):
#### ---------------READ FILE------------------ #####
    line1 = (file1.readline())
    [A, B, K] = [int(s) for s in line1.split()]
        
    count = 0
    C = []


#### ---------------ACTUAL FUNCTION------------- #####
    #variables: You have  N_LIST
    for a in xrange(A):
        for b in xrange(B):
            x =(a&b)
            if x < K:
                count += 1
    
    return count
    
    
'''
#### ------------------------------------------------------------------ #####
#-END FUNCTION-# 
#### ------------------------------------------------------------------ #####
'''   
#### -------------------PRINTING PART DON'T TOUCH-------------------- #####

caseNumber = int(file1.readline())

for caseN in range(caseNumber):
    N = caseN + 1
    print N
    ans = magicFunction(file1)

    #print ("Case #"+str(N)+ '' +  ":" + ' ' + str(ans) + '\n')
    file2.write("Case #"+str(N)+ '' +  ":" + ' ' + str(ans) + '\n')

file2.close()

