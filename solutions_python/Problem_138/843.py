
def score_normal(n, a, b):
    ans = 0
    for x in a:
        best = -1
        for v in b:
            if v > x and (best == -1 or v < best):
                best = v
        if best == -1:
            best = min(b)
        if x > best:
            ans += 1
        b.remove(best)
        
    return ans

def score_cheat(n, a, b):
    ans = 0
    a.sort()
    b.sort()
    
    for lose in xrange(0, n):
        tmp = 0
        for j in xrange(lose, n):
            if a[j] > b[j-lose]: tmp += 1
        if tmp > ans:
            ans = tmp
        
    return ans

if __name__ == '__main__':
    T = input()
    for tnum in range(1, T + 1):
        
        n = input()
        a = map(float, raw_input().strip().split())
        b = map(float, raw_input().strip().split())
        
        cheat = score_cheat(n, a[:], b[:])
        normal = score_normal(n, a[:], b[:])

        print 'Case #%d: %d %d' % (tnum, cheat, normal)
