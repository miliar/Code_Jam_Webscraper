##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(a1,F1,a2,F2):
    
    res = [item for item in F1[a1-1] if item in F2[a2-1]]

    if res==[]:
        return "Volunteer cheated!"
    if len(res)>1:
        return "Bad magician!"
    return str(res[0])
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    a1 = int(input())
    F1 = [[int(item) for item in input().rstrip().split()] for _ in range(4)]

    a2 = int(input())
    F2 = [[int(item) for item in input().rstrip().split()] for _ in range(4)]
  
    ## solve and print result
    result = solve(a1,F1,a2,F2)
    print('Case #'+str(t+1)+': '+str(result))
