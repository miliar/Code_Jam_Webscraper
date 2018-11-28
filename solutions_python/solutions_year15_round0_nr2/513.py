import heapq as h


def solve(case):
    D = int(raw_input().strip())
    X = map(int, raw_input().strip().split())
    
    Memo = {}

    def find(C):
        if C in Memo:
            return Memo[C]
        
        ma = None
        for i in xrange(9, 0, -1):
            if C[i]:
                ma = i
                break
        if ma <= 3:
            return ma
        ans = ma
        for i in xrange(1, ma / 2 + 1):
            j = ma - i
            newC = list(C)
            newC[ma] -= 1
            newC[i] += 1
            newC[j] += 1
            ans = min(ans, 1 + find(tuple(newC)))
        Memo[C] = ans
        return ans
    
    C = [0] * 10
    for i in X:
        C[i] += 1
    ans = find(tuple(C))
    print "Case #%d: %d" % (case, ans)


def _solve(case):
    D = int(raw_input().strip())
    X = map(int, raw_input().strip().split())

    # do nothing
    ans = max(X)

    H = [-i for i in X]
    h.heapify(H)
    
    # special minutes
    t = 0
    while H and t < ans:
        v = -h.heappop(H)
        # no special min from now on
        ans = min(ans, t + v)
        # special min: divide largest value
        if v <= 2:
            break
        if v & 1:
            h.heappush(H, -v / 2)
            h.heappush(H, -(v + 1) / 2)
        else:
            h.heappush(H, -v / 2)
            h.heappush(H, -v / 2)
        t += 1

    print "Case #%d: %d" % (case, ans)


if __name__ == '__main__':
    T = int(raw_input().strip())
    for t in xrange(1, T+1):
        solve(t)
