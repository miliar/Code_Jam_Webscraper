#!/usr/bin/python

def opstoremove(armon, unadded):
    return len(unadded)

def opstoadd(armon, unadded):
    if armon < 2:
        return 10**25
    x = armon
    ops = 0
    while x <= unadded[0]:
        x = x*2 - 1
        ops += 1
    return ops

def getans(armon, unadded):
 #   print armon
    unadded.sort()
    unadded = sorted(unadded)
    ops = 0
    l = len(unadded)
    
    for _ in range(l):
        if opstoadd(armon, unadded) >= opstoremove(armon, unadded):
            ops += 1
            unadded.pop(0)
        elif armon > unadded[0]:
            armon += unadded[0]
            unadded.pop(0)
        else:
            ops1 = ops
            armon1 = armon
            while armon1 <= unadded[0]:
                armon1 = armon1*2 - 1
                ops1 += 1
#                print armon1
            armon1 = armon1 + unadded[0]
            unadded.pop(0)
            ops += 1
#            print ops + len(unadded)
            ops = min(ops + len(unadded), ops1 + getans(armon1, unadded[:]))
            break
    return ops


casenum = int(raw_input())
armon = 0
others = 0
unadded = []
answer = 0

for c in range(1, casenum+1):
    s = raw_input()
    armon = int(s.split()[0])
    others = int(s.split()[1])
    s = raw_input()
    unadded = [int(x) for x in s.split()]
    answer = getans(armon, unadded)
    print "Case #{}: {}".format(c, answer)
