def recycled(L):
    cands = [int(("").join(L))]
    tmp = L[:]
    tmp.append(tmp.pop(0))
    while(tmp != L):
        cands.append(int("".join(tmp[:])))
        tmp.append(tmp.pop(0))
    return cands

def calc(beg, end):
    S = set()
    cnt = 0
    for i in xrange(beg, end+1):
        if i>= 10:
            if i in S:
                continue
            cands = recycled(list(str(i)))
            if len(cands) > 1:
                for j in cands:
                    S.add(j)
                point = len([j for j in cands if i <= j <= end])
                if point > 1:
                    cnt += point * (point-1) / 2
    return cnt

def solve(io):
    N = int(io.readline().strip())
    for i in xrange(N):
        beg, end = [int(x) for x in io.readline().split(" ")]
        print "Case #%d: %d" % (i+1, calc(beg, end))

# print calc(1, 9)
# print calc(10, 40)
# print calc(100, 500)
# print calc(1111, 2222)
if __name__ == "__main__":
    import sys
    solve(sys.stdin)
