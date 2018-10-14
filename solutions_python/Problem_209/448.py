from math import pi

def best_sa_bottom(l, k):
    return sum(sorted([x[0]*x[1] for x in l], reverse=True)[:min(k, len(l))])*2

def best_sa(l, k):
    l = sorted(l, key=lambda x:-x[0])
    return max([best_sa_bottom(l[i + 1:], k - 1) + l[i][0]**2 + 2*l[i][0]*l[i][1] for i in range(len(l))])*float(pi)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inp = raw_input().split(" ")
    n = int(inp[0])
    k = int(inp[1])
    l = []
    for _ in range(n):
        inp = raw_input().split(" ")
        r = int(inp[0])
        h = int(inp[1])
        l.append((r, h))
    print "Case #{}: {}".format(i, best_sa(l, k))
