import math
import collections

t = int(input())
for r in range(t):
    sn,p = map(int,input().split(' '))
    mapping = {}
    mapping[sn] = 1
    count = 0


    while count < p:


        if sn % 2 == 0:
            Max = math.ceil(sn / 2)
            min = sn - Max - 1
        elif sn %2 != 0:
            Max =  math.floor(sn / 2)
            min = Max
        howMany = mapping.get(sn)
        mapping[Max] =  mapping.get(Max,0) + 1*howMany
        mapping[min] = mapping.get(min,0) + 1*howMany
        del mapping[sn]
        sn = max(mapping.keys())
        count = count + 1 + howMany - 1

    print("Case #%s: %s %s" % (r + 1, Max,min ))










