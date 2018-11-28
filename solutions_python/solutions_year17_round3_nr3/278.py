def solve(test):
    n, k = map(int, raw_input().split())

    u = float(raw_input())

    p = map(float, raw_input().split())

    p.sort()

    i=0

    while u>0 and i<n:
        while i<n and p[i]==p[0]:
            i+=1

        if i<n:
            mx = p[i]
        else:
            mx = 1
            
            
        r = (mx-p[0])*i

        if u>=r:
            u -= r
            for j in xrange(i):
                p[j] = mx            
        else:            
            for j in xrange(i):
                p[j]+=u/i
            u = 0

        
    q = 1    
    for i in xrange(n):
        q *= p[i]

    print q

import sys
sys.stdin = open(sys.argv[1] if len(sys.argv) > 1 else "sample.in")

for test in range(input()):
    print "Case #{}:".format(test+1),
    answer = solve(test)
    if answer != None:
        print answer


