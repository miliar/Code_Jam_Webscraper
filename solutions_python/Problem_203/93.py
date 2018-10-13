##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(r,c,cake):
    f = [[item for item in row] for row in cake]

    ## just fill up lines horizontally (in both directions)
    for y in range(r):
        for x in range(c-1):
            if f[y][x+1]=='?':
                f[y][x+1] = f[y][x]
        for x in range(c-1,0,-1):
            if f[y][x-1]=='?':
                f[y][x-1] = f[y][x]

    ## now only blank lines can be left
    for y in range(r-1):
        if f[y+1].count('?')==c:
            f[y+1] = list(f[y])
    for y in range(r-1,0,-1):
        if f[y-1].count('?')==c:
            f[y-1] = list(f[y])
        
    return ["".join(item) for item in f]            
    
                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    r,c = [int(item) for item in input().rstrip().split()]
    cake = [input().rstrip() for _ in range(r)]    
    ## solve and print result
    result = solve(r,c,cake)
    print('Case #'+str(t+1)+': ')
    for item in result:
        print(item)

    
