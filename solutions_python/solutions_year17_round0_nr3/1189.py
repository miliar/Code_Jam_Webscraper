#s = "-+++-"    #state
#k = 4          #the num of pancakes
import math
def oldplacePeople(N,k):
    stalls=[N]
    for i in xrange(k):
        M = max(stalls)
        new = stalls.index(M)
        myLeft = int(math.floor((M-1)/2.0))
        myRight = int(math.ceil((M-1)/2.0))
        stalls = stalls[:new]+[myLeft,myRight]+stalls[new+1:]
    return max([myLeft,myRight]),min([myLeft,myRight])
    #print stalls 

def placePeople(N,k):
    depth=int(math.floor(math.log(k,2)))
    takenSeats = pow(2,depth)-1.0
    numInLevel = k+1-pow(2,depth)
    
    backetInRow=pow(2,depth)+0.0
    leftSeats = (N-takenSeats)
    
    if numInLevel<=(leftSeats%backetInRow):
        M=math.ceil(leftSeats/backetInRow)
    else:
        M=math.floor(leftSeats/backetInRow)
    myLeft = int(math.floor((M-1)/2.0))
    myRight = int(math.ceil((M-1)/2.0)) 
    return max([myLeft,myRight]),min([myLeft,myRight])
    
    

#print placePeople(1000,1)
#print placePeople(500000,250000)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, k = [int(x) for x in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #print N,k
  res = placePeople(N,k)
  print "Case #{}: {} {}".format(i, res[0], res[1])
  # check out .format's specification for more formatting options
