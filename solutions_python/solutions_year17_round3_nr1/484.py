import math
t = int(raw_input())

for i in xrange(t):
    n, k = map(int, raw_input().split(' '))
    rh = []
    ans = 0
    for j in xrange(n):
        r, h = map(float, raw_input().split(' '))
        rh.append((r,h))

    rh.sort()
    for j in xrange(n-1, k-2,-1):
        firstRH = rh[j]
        left = rh[:j]
        rhr = []
        for r,h in left:
            rhr.append((h*r,h,r))
        rhr.sort(reverse=True)
        temp = firstRH[0] * firstRH[0] + 2*firstRH[1] * firstRH[0] 
        for x in xrange(k-1):
            temp += 2 * rhr[x][1] * rhr[x][2]
        temp = math.pi * temp
        ans = max(ans,temp)
    print 'Case #{}: {:.9f}'.format(i+1, ans)