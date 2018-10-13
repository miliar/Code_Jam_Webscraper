file = open("c:/CodeJam/problemB/B-small-attempt1.in")
line = file.next()

def fastpancake(P):
    """Calculates Fastest Way to perform N splits on a single stack of panckes"""
    P.sort()
    maxtime=P[-1]
    
    for i in range(2,P[-1]/2+1):
        Pi=[]
        Pi.extend(P[0:-1])
        Pi.extend([P[-1]-i,i])
        ##print Pi
        flips=1
        newmaxtime=fastpancake(Pi)+1
        if newmaxtime<maxtime:
            maxtime=newmaxtime
    return maxtime

## Number of Test Cases:  1<=T<=100
T=int(line)
## Tests each case
for testcase in range(T):
    ## D: Number of Diners with Pancakes
    D = file.next()
    ## P: List of Pancake Depths
    P= (file.next()).split()
    ## Converts string into ints
    P= [ int(Pi) for Pi in P]
    
    
    print('Case #{}: {}'.format(testcase+1,fastpancake(P)))
           
        
        
            
    

    
    

