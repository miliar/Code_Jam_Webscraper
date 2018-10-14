import sys

##            
## PROBLEM SOLVING ALGORITHM 
##  
def solve(x,r,c):
    if c<r:
        r,c = c,r

    # for ominos of size 7 and bigger, omino with 1 hole can be
    # found -> win
    if x>=7:
        return True

    # is remainder condition fullfilled?
    if (r*c)%x != 0:
        return True

    # test straight omino
    if x>c:
        return True

    # symmetric L-shaped omino
    if x>=2*r+1:
        return True

    # omino too small to divide grid
    if x<2*r-1:
        return False

    # try to divide grid with remaining areas not divisible by x
    width = x-r+1
    for a in range(r*width+1-x):
        divided = True
        for i in range(c-width+1):
            if (a+i*r)%x==0:
                divided = False
        if divided:
            return True

    return False
        

                    
##            
## MAIN LOOP: read(from stdin) - solve - print(to stdout) 
##
T = int(input())
for t in range(T):
    
    ## read case
    x,r,c = [int(item) for item in input().rstrip().split()]
        
    ## solve and print result
    if solve(x,r,c):
        result = "RICHARD"
    else:
        result = "GABRIEL"
    print('Case #'+str(t+1)+': '+str(result))

    ## progress output
    print('Done: '+str(t+1)+' of '+str(T), file=sys.stderr)
