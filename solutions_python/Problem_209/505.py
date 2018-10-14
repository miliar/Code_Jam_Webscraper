import math
import copy
def pour(n,k,p):
    mul = []
    sqr = []
    for r,h in p:
        mul.append(2*r*h)
        sqr.append(r**2)
    mul1 = copy.deepcopy(mul)
    p1 = copy.deepcopy(p)
#Case 1
    p = [x for (y,x) in sorted(zip(mul,p))]
    mul.sort()
    sel = p[-k:]
    selm = mul[-k:]
    a = sum(selm) + max(sel)[0]**2
    
#Case 2
    m = max(sqr)
    msqi = [i for i, j in enumerate(sqr) if j == m]
    j = msqi[0]
    for i in msqi:
        if(mul1[i] > mul1[j]):
            j = i
    r0, h0= p1.pop(j)
    selm1 = [mul1.pop(j)]
    mul1.sort()
    if(1-k < 0):
        selm1.extend(mul1[1-k:])
    b = sum(selm1) + r0**2

    return math.pi * max(a,b)

    
    




# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    p = []
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    for j in range(n):
        p.append([int(s) for s in input().split(" ")])
    y = pour(n,k,p)
    print("Case #{}: {}".format(i, y))
# check out .format's specification for more formatting options
 