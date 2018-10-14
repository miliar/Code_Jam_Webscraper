
def solve():
    n, x = map(int, raw_input().split())
    ss = map(int, raw_input().split())
    d = {}
    for s in ss:
        d.setdefault(s, 0)
        d[s] += 1
    ans = 0
    while True:
        j = -1
        for i in xrange(700, 0, -1):
            if d.get(i, 0) > 0:
                j = i
                break
        if j == -1:
            return ans
        d[j] -= 1
        ans += 1
        r = x - j
        for i in xrange(r, 0, -1):
            if d.get(i, 0) > 0:
                d[i] -= 1
                break

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        print 'Case #%s: %s' % (i, solve())

if __name__ == '__main__':
    main()
