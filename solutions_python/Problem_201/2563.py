import sys

DEBUG=True
DEBUG=False

def next_pos(free):
    l, r, pos = -1, -1, 0
    for i in xrange(len(free)):
        if free[i]:
            li = 0
            j = i-1
            while j >=0 and free[j]:
                li += 1
                j -= 1
            ri = 0
            j = i+1
            while j < len(free) and free[j]:
                ri += 1
                j += 1
            if DEBUG: print i, li, ri
            if min(li, ri) > min(l, r):
                l, r, pos = li, ri, i
            elif min(li, ri) == min(l, r) and max(li, ri) > max(l, r):
                l, r, pos = li, ri , i
    if DEBUG: print "found", l, r, pos
    return l, r, pos

def solve(n, k):
    free = [True for _ in range(n)]
    for _ in xrange(k-1):
        _, _, pos = next_pos(free)
        free[pos] = False
        #if DEBUG: print pos, free
    l, r, pos = next_pos(free)
    if DEBUG: print l, r, pos
    return l, r

if __name__ == "__main__":
    i = 1
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        n = int(data.pop(0))
        k = int(data.pop(0))
        l, r = solve(n, k)
        print "Case #%d: %s %s" % (i, max(l, r), min(l, r))
        i += 1
