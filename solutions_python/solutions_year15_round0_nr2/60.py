import sys

##            
## PROBLEM SOLVING ALGORITHM 
##

def solve(pancakes):
    res = None
    ## test eating times 1..max number of pancakes on one plate
    for t in range(1,max(pancakes)+1):

        # for every plate check number of special minutes for 
        # distribution needed in order to achieve given eating time
        specialMinutes = 0
        for plate in pancakes:
            n = plate//t
            if (plate%t)!=0:
                n += 1
            specialMinutes += (n-1)
        if res==None or (specialMinutes+t<res):
            res = specialMinutes+t
            
    return res
           
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    d = int(input())
    pancakes = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    result = solve(pancakes)
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
