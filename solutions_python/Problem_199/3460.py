from itertools import groupby


def flip(cakes, s, size):
    if s + size > len(cakes):
        return -1
    else:
        flipped = cakes[:s]
        
        for i in range(s, s+size):
            if cakes[i] == '-':
                flipped += '+'
            else:
                flipped += '-'
                
        flipped += cakes[s+size:]
        
        return flipped

## I/O
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
    pancakes, size = raw_input().split(" ")  # read a list of integers, 2 in this case
    size = int(size)
    
    ## My Code
    y = 0
    for x in range(len(pancakes)):
        if pancakes[x] == '-':
            pancakes = flip(pancakes, x, size)        
            if pancakes == -1:
                y = "IMPOSSIBLE"
                break;
            else:
                y += 1
                
    print "Case #{}: {}".format(i, y)
     
