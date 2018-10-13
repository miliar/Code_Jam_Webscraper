import math
C = int(raw_input())

def dist(a, b):
    return (a[2] + b[2] + math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))/2.0

def solve(case):
    N = int(raw_input())    
    plants = []
    for i in xrange(N):
        plants.append(map(int, raw_input().split()))
    
    if N == 1:
        ans = plants[0][2]
    elif N == 2:
        ans = max(plants[0][2], plants[1][2])
    elif N == 3:
        ans = None
        for i in xrange(3):
            if ans is None:
                ans = max(plants[i][2], dist(plants[i-1], plants[i-2]))
            else:
                ans = min(ans, max(plants[i][2], dist(plants[i-1], plants[i-2])))
    
    print "Case #%d: %.6f" % (case, ans)

for i in xrange(1, C+1):
    solve(i)
