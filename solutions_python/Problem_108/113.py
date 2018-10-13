import sys

def main():
    with sys.stdin as f:
        for x in range(int(f.readline())):
            print "Case #%d: %s" % (x+1, str(solve(f)))

def solve(f):
    N = int(f.readline())
    d = []
    l = []
    for x in range(N):
        nd, nl = [int(n) for n in f.readline().split()]
        d.append(nd)
        l.append(nl)
    D = int(f.readline())
    return "YES" if possible(d, l, D) else "NO"

def possible(d, l, D, pos=0):
    if len(d) == 0:
        return False
    if d[0] - pos + d[0] >= D:
        return True
    branches = reachable(d, D, pos)
    if len(branches) == 0:
        return False
    for i in branches[::-1]:
        if possible(d[i:], l[i:], D, max(d[0], d[i] - l[i])):
            return True
    return False


def reachable(d, D, pos):
    l = d[0] - pos
    ml = d[0] + l
    ans = []
    for i in range(len(d[1:])):
        if d[i+1] > ml:
            break
        ans.append(i+1)
    return ans

def end(pos, vine, d, l, D):
    swing = d[vine] - pos
    end = d[vine] + swing
    return True if end >= D else False

def options(pos, vine, d, l):
    swing = d[vine] - pos
    end = d[vine] + swing
    nvine = vine + 1
    if nvine >= len(d) or d[nvine] > end:
        return None
    length = 0
    pos = 0
    gvine = 0
    while nvine < len(d):
        if d[nvine] <= end:
            nl = min(d[nvine] - d[vine], l[nvine])
            np = d[nvine] - nl
            if nl > length:
                gvine = nvine
                length = nl
                pos = np
            nvine += 1
        else:
            break
    return pos, gvine
        

if __name__ == '__main__':
    main()
