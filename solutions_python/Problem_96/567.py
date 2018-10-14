import sys

def surprise(total):
    if total == 0: return 0
    return total/3 + (2 if total%3 == 2 else 1)

def default(total):
    return total/3 + (0 if total%3 == 0 else 1)

def main(source):
    next(sys.stdin)
    for i, l in enumerate(sys.stdin):
        l = map(int, l.split())
        N, S, p = l[:3]
        totals = l[3:]
        assert len(totals) == N
        default_n = sum(1 for t in map(default, totals) if t >= p)
        surprise_n = sum(1 for t in map(surprise, totals) if t >= p)
        assert (surprise_n >= default_n)
        improved = surprise_n - default_n
        final = min(default_n+S, default_n+improved, totals)
        print('Case #%d: %s' % (i+1, final))

if __name__ == '__main__':
    main(sys.stdin)

