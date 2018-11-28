import sys
sys.setrecursionlimit(10000000)
"""
def solve(C,F,X,income,timetaken):
    if X/(income + 0.0) <= C/(income + 0.0) + X/(income + F):
        return timetaken + X/(income + 0.0)

    else:
        timetaken += C/income
        cookies = 0
        income += F
        print X/income, C/(income) + X/(income + F), timetaken
        return solve(C,F,X, income, timetaken)
"""

def solve(C,F,X,income,timetaken):
    # income -> current rate of earning cookies.

    #X/income -> time taken if we don't buy the factory
    # C/income + X/(income + F) -> time taken if we buy the factory

    if X/(income + 0.0) <= C/(income + 0.0) + X/(income + F):
        return timetaken + X/(income + 0.0)

    #if abs(X/(income + 0.0) - (C/(income + 0.0) + X/(income + F))) < pow(10, -8):
    #    return timetaken + X/(income)

    else:
        timetaken += C/income
        cookies = 0
        income += F
        
        #print X/income, C/(income) + X/(income + F), timetaken
        return solve2(C,F,X, income, timetaken)





def solve2(C,F,X,income,timetaken):
    # income -> current rate of earning cookies.

    #X/income -> time taken if we don't buy the factory
    # C/income + X/(income + F) -> time taken if we buy the factory

    timetaken += C/income

    if (X - C)/(income + 0.0) <= X/(income + F):
        return timetaken + (X - C)/(income + 0.0)

    #if abs(X/(income + 0.0) - (C/(income + 0.0) + X/(income + F))) < pow(10, -8):
    #    return timetaken + X/(income)

    else:
        #timetaken += C/income
        cookies = 0
        income += F
        
        #print X/income, C/(income) + X/(income + F), timetaken
        return solve2(C,F,X, income, timetaken)



T = int(sys.stdin.readline())
for casenum in xrange(T):
    a = map(float, sys.stdin.readline().strip().split(' '))
    C,F,X = a[0], a[1], a[2]

    print 'Case #%d: %.7f' % (casenum + 1, solve2(C,F,X, 2.0, 0.0))

#print solve2(C,F,X, 2.0, 0.0, 0)


C = 1.00508
F = 3.96431
X = 1999.11727
#print solve2(C,F,X,2.0,0)
