import sys

##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(s_max,s):
    stand = 0
    friends = 0
    
    # simulate stand up
    for level in range(s_max+1):
        # check if friends are needed for next level
        neededFriends = max(level-stand,0)
        stand += int(s[level]) + neededFriends 
        friends += neededFriends
        
    return friends
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    data = input().rstrip().split()
    s_max = int(data[0])
    s = data[1]
        
    ## solve and print result
    result = solve(s_max,s)
    print('Case #'+str(t+1)+': '+str(result))

