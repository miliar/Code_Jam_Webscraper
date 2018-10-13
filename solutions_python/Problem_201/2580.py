from heapq import heapify, heappop, heappush
inputfile="stall.in"
putput="stall.out"
from math import pow
data = [row.replace("\n",'').split(" ") for row in open(inputfile, "r").readlines()][1:]

def intera(n, k):
    
    choices = []
    choices.append(tuple([n-n, 0, n]))

    while(k > 0):
        a = heappop(choices)
        k -= 1
        m = (a[1] + a[2]) // 2
        if k > 0 and (a[2] - a[1] > 1):
            l1 = m - a[1]
            l2 = a[2] - (m + 1)
            if  l1 > 0:
                heappush(choices, tuple([n-l1, a[1], m]))
            if l2  > 0:
                heappush(choices, tuple([n-l2,m +1, a[2]]))
        else:
            L_s = m - a[1]
            R_s = a[2] - (m + 1)
            v = [L_s, R_s]
            return (max(v), min(v))
            #ærrivati





vals = list()
for case in data:
    n = int(case[0])
    k = int(case[1])
    vals += [intera(n, k)]

f = open("stall.out", "w")
i = 1
for v in vals:
    f.write("Case #{}: {} {}\n".format(i, v[0], v[1]))
    i += 1