# Google Code Jam 2012 qualification round B.
# unsurpLimit - total this or greater wins
# surpLimit - total this or greater surprising wins
# 1 1 1: 3
# 1 1 2: 4
# 1 2 2: 5
# 1 1 3: 5
# for best >= p, total unsurprising >= 3p-2
# total surprising >= 3p - 4

import sys
def doCase(N, S, p, t):
    result = 0
    for tot in t:
        if tot >= 3*p-2: result += 1
        elif tot >= 3*p-4 and tot >= p and S > 0:
            S -= 1
            result += 1
    return result

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        line = map(int, file.readline().split())
        (N,S,p) = line[0:3]     # num googlers, num surprising
        t = line[3:]            # totals
        answer = doCase(N, S, p, t)
        print 'Case #{0}: {1}'.format(case, answer)
run()
