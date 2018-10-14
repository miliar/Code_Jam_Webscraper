#!/usr/bin/python




def cread(fd):
    return fd.readline().strip('\n')



def solve(fd):

    N, L, H = [ int(x) for x in cread(fd).split() ]
    Freq = set([ int(x) for x in cread(fd).split() ])

    # Build the list of candidates:
    for opt in xrange(L,H+1):
        for f in Freq:
            if opt%f!=0 and f%opt!=0:
                break
        else:
            return str(opt)
    return "NO"
    
    



import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = int(cread(fd))

for i in xrange(T):
    sol = solve(fd)
    print("Case #%d: " % (i+1) + sol)
    
fd.close()
    
    
    
        
        



