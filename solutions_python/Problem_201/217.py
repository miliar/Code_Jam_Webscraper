import sys

def main():
    with open(sys.argv[1]) as f, open(sys.argv[1] + '.out', 'w') as out:
        T = int(next(f))
        for i in xrange(T):
            N, K = map(int, next(f).split())
            ls, rs = solve(N, K)
            out.write('Case #%d: %d %d\n' % (i+1, ls, rs))

def solve(N, K):
    i = 1
    j = 1
    segs = {N: 1}
    while i < K:
        tmp = {}
        for key in segs:
            tmp[(key-1)//2] = tmp.get((key-1)//2, 0) + segs[key]
            tmp[key//2] = tmp.get(key//2, 0) + segs[key]
        segs = tmp
        j *= 2
        i += j
    index = K - (i - j)
    for key in sorted(segs, reverse=True):
        if index > segs[key]:
            index -= segs[key]
        else:
            return key//2, (key-1)//2

if __name__ == '__main__':
    main()
