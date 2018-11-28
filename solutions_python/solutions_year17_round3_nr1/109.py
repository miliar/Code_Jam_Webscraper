import random

import math
PI = math.pi
def solve(n, chosen, pancakes):
    pancakes.sort(reverse=True)

    m = [[0,] * (n+1) for i in xrange(n+1)]
    m[0][0] = 0

    for i in xrange(1, n+1):
        rad, height = pancakes[i-1]
        m[i][1] = max(m[i-1][1], 2*rad*PI*height + PI*rad**2)
    
    for i in xrange(1, n+1):
        for j in xrange(2, n+1):
            rad, height = pancakes[i-1]
            additional = rad * PI *height * 2
            most = 0

            
            most = max(most, m[i-1][j-1]+additional, m[i-1][j])
            m[i][j] = most

            
    return m[n][chosen]

# n = 1000
# chosen = 50
# pancakes = []
# for i in xrange(n):
#     pancakes.append((random.randint(1, 10**6), random.randint(1, 10**6)))
# print solve(n, chosen, pancakes)

for i in xrange(input()):
    n, k = map(int, raw_input().split(' '))
    pancakes = []
    for j in xrange(n):
        pancakes.append(map(int, raw_input().split(' ')))

    print "Case #%d: %f" % (i+1, solve(n, k, pancakes))