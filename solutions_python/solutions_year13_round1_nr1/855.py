import math

for x in range(int(raw_input())):
    d = [int(j) for j in raw_input().split(' ')]
    r, t = d[0], d[1]
    
    y = int(((1 - 2*r + math.sqrt(math.pow(2*r - 1, 2) + 8*t))/4))
    
    print "Case #%d: %s" % (x+1, y)
