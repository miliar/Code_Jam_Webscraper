import sys

TN = int(sys.stdin.readline()[:-1])

for i in range(TN):
    line = sys.stdin.readline()[:-1]
    ns = [int(e) for e in line.split()]
    N = ns[0]
    S = ns[1]
    p = ns[2]
    ps = ns[3:]
    ps.sort(reverse=True)
    ret = 0
    for c in ps:
        if p * 3 <= c:
            ret += 1
            continue
        if p * 3 - 2 <= c and p - 1 >= 0:
            ret += 1
            continue
        if S > 0:
            if p * 3 - 4 <= c and p-2 >= 0:
                S -= 1
                ret += 1
                continue
            else:
                break
        else:
            break 
    print "Case #%d: %d" % (i+1, ret)

