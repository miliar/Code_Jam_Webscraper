# Google Code Jam

def coaster(IN):
    pass
    # Input is of the form
    # T, # of test cases
    # R k N, R coaster runs, k people per run, N groups of people
    # g0 g1 g2 ... gn, # of people in each group

    # Parse each TestCase, store R k N, and a list of groups
    f = open(IN)
    T = f.readline().strip()
    bigList = []
    for i in range(0,int(T)):
        tmp = []
        tmp.extend(f.readline().strip().split())
        tmp.append(f.readline().strip().split())
        bigList.append(tmp)
    # Our big-list has the format [[R,k,N,[g0,g1..,gN]],[R,k,N,[g0,g1..,gN],...]
    print bigList
    sol = []
    for i in bigList:
        #Loops over our bigList, and calculates the Euros earned.
        eurosEarned = 0
        coasterRuns = int(i[0])
        totalGroupSize = 0
        listPtr = 0
        for j in range(1,coasterRuns+1):
            #Loops over the number of coaster runs per day
            groupsSeen = 0
            spaceLeft = int(i[1])
            while ((spaceLeft > 0) and (groupsSeen < int(i[2]))):
                spaceLeft -= int(i[3][listPtr])
                groupsSeen += 1
                if spaceLeft < 0:
                    break
                eurosEarned += int(i[3][listPtr])
                listPtr = (listPtr + 1) % int(i[2])
        sol.append(eurosEarned)
    print sol
    printOutput(sol)
def printOutput(list1):
    # List is of the form Case #x: y
    # where x is the case #(starting from 1)
    # and y is either "ON", or "OFF"
    f = open('./out.txt','w')
    for i in range(1,len(list1)+1):
        string = 'Case #'+str(i)+': '+str(list1[i-1])
        f.write(string + '\n')

#Initially the vector 0*n exists, representing the on/off
#Initially the vector 1, 0*(n-1) exists, representing the power on/off

#To calculate a new on/off vector after k switches we add
#the previous on/off, power on/off vectors

#To calculate a new power on/off vector we check if it's odd
#if yes, then it's 1, 0*(n-1)
#else, the it's 
##a b c d e f 
##0 0 0 0 0 0 o/f
##1 0 0 0 0 0 rp
##
##1
##1 0 0 0 0 0
##1 1 0 0 0 0
##
##2
##0 1 0 0 0 0
##1 0 0 0 0 0
##
##3
##1 1 0 0 0 0
##1 1 1 0 0 0
##
##4
##0 0 1 0 0 0
##1 0 0 0 0 0
##
##5
##1 0 1 0 0 0
##1 1 0 0 0 0
##
##6
##0 1 1 0 0 0
##1 0 0 0 0 0
##
##7
##1 1 1 0 0 0
##1 1 1 1 0 0
##
##8
##0 1 1 0 0 0
##1 0 0 0 0 0
##
##9
##1 1 1 0 0 0
##1 1 1 1 0 0
##
##10
##0 0 0 1 0 0
##1 0 0 0 0 0
##
##11
##1 1 0 1 0 0
##1 1 1 0 0 0
##
##12
##1 1 1 1 0 0
##1 1 1 1 1 0
