import math
inp=open('A-small-attempt2.in','r')
test=int(inp.readline().rstrip('\n'))
for counter in range(1,test+1):
    given=inp.readline().rstrip('\n').split(' ')
    r=int(given[0])
    t=int(given[1])
   
    base=2*r+1
    target=t
    guess=int(((2-base)+math.sqrt(((base-2)**2)+(8*t)))/(4))
    g=guess*(base-2) + (guess**2)*2 
    while(g>t):
        guess=guess-1
        g=guess*(base-2) + (guess**2)*2
        
    print "Case #%d: %d"%(counter,guess)
    
