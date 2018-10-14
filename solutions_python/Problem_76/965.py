import sys
import math
def solve(candies):
    maxx = max(candies);
    if maxx == 0:
        return 0
    n =  int(math.floor(math.log(maxx, 2)))
    for i in range(n, -1, -1):
        col = []
        for c in candies:
            col.append((c >> i) % 2)        
        if sum(col) % 2 == 1:
            return "NO" 
    return sum(candies) - min(candies)
    

f = open(sys.argv[1], 'r')
t = int(f.readline())
case = 0
while t>0:
    n = int(f.readline())
    candies = map(int, f.readline().split())
    t -= 1
    case += 1
    print "Case #%d: %s" % ( case, solve(candies) )

