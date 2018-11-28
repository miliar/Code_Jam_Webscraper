import sys
#sys.stdin = open("c.txt")

N = (10 ** 5)

def float_2_int(f):
    return int(float(f) * N + 1e-4)

if __name__ == '__main__':
    T = int(raw_input())
    for case_ in xrange(T):
        print 'Case #%d:' % (case_ + 1),
        (n, k) = map(int, raw_input().split())

        assert n == k

        tot = float_2_int(float(raw_input()))

        ns = map(float_2_int, map(float, raw_input().split()))

        ans = 0
        for i in xrange(0, N + 1):
            s = 0
            res = 1
            nns = []
            cnt = 0
            for item in ns:
                if item < i:
                    s += (i - item)
                    res *= i
                    nns.append(i)
                    cnt += 1
                else:
                    res *= item
                    nns.append(item)
                    
            

            if s <= tot:
                nns.sort()
                if tot - s:
                    for i in xrange(cnt):
                        nns[0] += 1.0 * (tot - s) / cnt
                ans = max(ans, reduce(lambda x, y: x * y, nns))
        print '%.10lf' % (1.0 * ans / (N ** n))
