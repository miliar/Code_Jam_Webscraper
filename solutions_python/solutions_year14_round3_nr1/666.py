import math
import sys
from collections import defaultdict

def dividers(n):
    res = defaultdict(int)
    i = 2
    max_cand = int(math.sqrt(n))
    while i <= max_cand:
        if (n % i) == 0:
            while (n % i == 0) and (n > 1):
                res[i] += 1
                n //= i
            max_cand = int(math.sqrt(n))
        i += 1
    res[n] += 1
    if 1 in res:
        del res[1]
    return res

def test(i, f):
    p,q = (int(n) for n in f.readline().split("/"))
    p_div = dividers(p)
    q_div = dividers(q)
    common = True
    for d in q_div:
        if d != 2:
            if p_div[d] != q_div[d]:
                common = False
    if common and (q_div[2] >= p_div[2]):
        level = 0
        while p < q:
            p *= 2
            level += 1
        print("Case #%d: %d" % (i,level))
    else:
        print("Case #%d: impossible" % (i))

def main(f):
    t = int(f.readline())
    for i in range(t):
        test(i+1,f)

#main(open("input.txt"))
main(open("A-small-attempt0.in"))
#for i in range(1, 26):
#    print(i, dividers(i))
