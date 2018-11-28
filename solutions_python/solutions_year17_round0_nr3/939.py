from sys import stdin
from collections import defaultdict

def solve(k,n):
    gaps = defaultdict(lambda : 0)
    gaps[k] = 1
    while n > 1:
        biggest = max(gaps)
        count = gaps[biggest]
        
        #print n, biggest, count, gaps
        
        if count >= n:
            break
        
        del gaps[biggest]

        if biggest == 1:
            return (0,0)
        
        if biggest % 2 == 0:
            gaps[biggest/2] += count
            gaps[biggest/2-1] += count
        else:
            gaps[(biggest-1)/2] += 2*count
    
        n -= count
    
    biggest = max(gaps)
    if biggest % 2 == 0:
        return biggest/2, biggest/2-1
    else:
        return (biggest-1)/2, (biggest-1)/2
		
def parse(input):
    t = int(input.next())
    
    for i in range(t):
        line = input.next().split(" ")
        n = int(line[0])
        k = int(line[1])

        y,z = solve(n,k)
        
        print "Case #%d: %d %s" % (i+1, y, z)
		

parse(stdin)