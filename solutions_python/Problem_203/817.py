def hoge(R, C, rects):
    buf = [[False for j in range(C)] for i in range(R)]
    for k, v in rects.items():
        (ltr, ltc), (brr, brc) = v
        if ltr < 0 or ltc < 0: return 2
        if brr >= R or brc >= C: return 2
        for y in range(ltr, brr+1):
            for x in range(ltc, brc+1):
                if buf[y][x]:
                    return 2
                else:
                    buf[y][x] = True
    for b in buf:
        if not all(b):
            # print(R, C, rects)
            return 1
    return 0

def print_solution(R, C, rects):
    buf = [['?' for j in range(C)] for i in range(R)]
    for k, v in rects.items():
        (ltr, ltc), (brr, brc) = v
        if ltr < 0 or ltc < 0: return 2
        if brr > R or brc > C: return 2
        for y in range(ltr, brr+1):
            for x in range(ltc, brc+1):
                buf[y][x] = k
    for b in buf:
        print ''.join(b)
    return 0


def rec(R, C, rects):
    r = hoge(R, C, rects)
    if r == 0:
        print_solution(R, C, rects)
        return 0
    for k, v in rects.items():
        (ltr, ltc), (brr, brc) = v
        rects[k] = ((ltr-1, ltc), (brr, brc))
        r = hoge(R, C, rects)
        if r == 1:
            rr = rec(R, C, rects)
            if rr == 0:
                return 0
        elif r == 0:
            print_solution(R, C, rects)
            return 0
        rects[k] = ((ltr, ltc-1), (brr, brc))
        r = hoge(R, C, rects)
        if r == 1:
            rr = rec(R, C, rects)
            if rr == 0:
                return 0
        elif r == 0:
            print_solution(R, C, rects)
            return 0
        rects[k] = ((ltr, ltc), (brr+1, brc))
        r = hoge(R, C, rects)
        if r == 1:
            rr = rec(R, C, rects)
            if rr == 0:
                return 0
        elif r == 0:
            print_solution(R, C, rects)
            return 0
        rects[k] = ((ltr, ltc), (brr, brc+1))
        r = hoge(R, C, rects)
        if r == 1:
            rr = rec(R, C, rects)
            if rr == 0:
                return 0
        elif r == 0:
            print_solution(R, C, rects)
            return 0
        rects[k] = ((ltr, ltc), (brr, brc))
    return 2


def solve(Ss, R, C):
    rects = {}
    for y, s in enumerate(Ss):
        for x, c in enumerate(s):
            if not c == '?':
                rects[c] = ((y, x), (y, x))
    result = rec(R, C, rects)


def main():
    T = input()
    for i in range(T):
        R, C = map(int, raw_input().split())
        S = [raw_input() for j in range(R)]
        print 'Case #%d:' %(i+1)
        solve(S, R, C)

if __name__ == '__main__':
    main()
