file = open("c:/CodeJam/2017/Qualifier/A-small-attempt1.in")
line = file.readline()

## functions
def pancakeflip(s,k):
    pancakenumber=len(s)
    pancakearray=[]
    flips=pancakenumber-k+1
    for i in range(flips):
        sflip=list(s)
        for j in range(k):
            if sflip[i+j]==0:
                sflip[i+j]=1
            elif sflip[i+j]==1:
                sflip[i+j]=0
        if sflip not in pancakearray:
            pancakearray.append(list(sflip))
    return pancakearray

## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    #S=String of Pancake States; K=flipper size
    [S,K] = file.readline().split()
    # pancakestate = string converted to an array of 1's and 0's
    pancakes0=[]
    
    for each in S:
        if each=='-':
            pancakes0.append(0)
        if each=='+':
            pancakes0.append(1)
    flippable=1
    flipnumber=0
    solutionfound=0
    S0=[1]*len(S)

    PANCAKES=[]
    PANCAKEqueue=[]
    PANCAKES.append(S0)
    PANCAKEqueue.append(S0)
        
    while flippable==1:
        if pancakes0 in PANCAKES:
            #print('Already Solved')
            break
        flipnumber+=1
        #print('Flips= '+str(flipnumber))
        PANCAKEqueue2=[]
        for i in range(len(PANCAKEqueue)):
            currentstack=PANCAKEqueue.pop()
            #print('currentstack')
            #print(currentstack)
            arrayofflippedpancakes=pancakeflip(currentstack,int(K))
            #print('pancakes flipped')
            if pancakes0 in arrayofflippedpancakes:
                PANCAKES.append(pancakes0)
                solutionfound=1
                #print('solution found')
                break
            
            if solutionfound==1:
                #print('breaking?')
                break

            #print('right before checking flipped')
            for each1 in arrayofflippedpancakes:
                #print('flipped')
                #print(each1)
                if each1 not in PANCAKES:
                    #print('stack added to q2')
                    PANCAKES.append(each1)
                    PANCAKEqueue2.append(each1)
        
        PANCAKEqueue=list(PANCAKEqueue2)
        if len(PANCAKEqueue)==0:
            flippable=0


##    print('Pancakes= '+S)
##    print('K= '+K)
##    print (pancakestate)
    if pancakes0 in PANCAKES:
        flippable=1
    if flippable==1:
        print('Case #{}: {}'.format(testcase+1,flipnumber))
    elif flippable==0:
        print('Case #{}: {}'.format(testcase+1,'IMPOSSIBLE'))
           
        
        
        
    

    
    

