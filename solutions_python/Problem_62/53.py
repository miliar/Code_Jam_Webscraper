def solve(ropes):
    count = 0
    s = sorted(ropes, key = lambda r : r[0])
    for r in s:
        for r2 in s:
            if r2[0] > r[0] and r2[1] < r[1]:
                count += 1
                #print "bingo!", r, r2
    return count


import sys
f = open(sys.argv[1], 'r')
t = int(f.readline())
case = 0
while t>0:
    n = int(f.readline())
    ropes = []
    while n>0:
        ropes.append(map(int, f.readline().split())) 
        n -= 1
    t -= 1
    case += 1
    print "Case #%d: %s" % ( case, solve(ropes) )
    #print "done with dirs:", dirs

