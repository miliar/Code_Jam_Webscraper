import sys
sys.setrecursionlimit(15000)

def findit(prevfps, factime, prevtime, extrafps, facprice, goal):
    newfactime = (facprice/prevfps)
    newfps = (prevfps + extrafps)
    nowtime = factime + newfactime + (goal / newfps)
    if nowtime > prevtime:
        return prevtime
    else:
        return findit(newfps, factime+newfactime, nowtime, extrafps, facprice, goal)

n = input()
for iii in xrange(n):
    facPrice, extraFPS, goal = map(float, raw_input().split())
    ans = findit(2.0, 0.0, goal/2.0, extraFPS, facPrice, goal)
    print 'Case #%d: %.7f' % (iii+1, ans)
