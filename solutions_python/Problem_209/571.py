import math
from heapq import nlargest
t=int(input())
for i in range(1,t+1):
    n,k = map(int,input().split())
    l = []
    for j in range(n):
        r,h = map(int,input().split())
        # print (r,h)
        l.append((r,h,2*r*h))
    # print (sorted(l,reverse=True))
    l = sorted(l,reverse=True)
    # print(l)
    circum_areas = [x[2] for x in l]
    maxi = 0 #l[0][0]*l[0][0]+sum(circum_areas[m] for m in range(k))
    for m in range(n-k+1):
        total_area = l[m][0]*l[m][0] + circum_areas[m]
        total_area+= sum(nlargest(k-1,circum_areas[m+1:]))
        # print (m,total_area)
        if maxi < total_area:
            maxi = total_area

    print("Case #{}: {}".format(i, maxi*math.pi))
