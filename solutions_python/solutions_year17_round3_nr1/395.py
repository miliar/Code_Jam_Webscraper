t = int(input())
import copy
import math
for test in range(t):
    n,k = map(int, input().split())
    cakes = []
    for i in range(n):
        r,h = map(int, input().split())
        cakes.append((r,h))
    cakes.sort(reverse=True)
    result = -1
    for i in range(n - k + 1):
        rmax = cakes[i][0]
        testcakes = copy.deepcopy(cakes[i+1:])
        tempresult = cakes[i][0]*cakes[i][1]
        testcakes.sort(reverse=True, key = lambda x: x[0]*x[1])
        for i in range(k - 1):
            tempresult += testcakes[i][0]*testcakes[i][1]
        tempresult *= (2 * math.pi)
        tempresult += (rmax**2)*math.pi
        result = max(tempresult, result)
    print("Case #"+str(test + 1)+": "+str(result))
