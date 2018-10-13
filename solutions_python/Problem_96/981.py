
def zero_or_more(x):
    if x < 0:
        return 0
    return x

def solve(n, s, p, mx_sc):
    res = 0
    for sc in mx_sc:
        if sc >= p + 2 * zero_or_more(p - 1):
            res += 1
            continue
        if sc >= p + 2 * zero_or_more(p - 2) and s > 0:
            res += 1
            s -=1
            continue
    return res

def main():
    tc = int(raw_input())
    for i in xrange(tc):
        args = map(int, raw_input().split())
        print("Case #{}: {}".format(
            i + 1, 
            solve(args[0], args[1], args[2], args[3:])))

if __name__ == '__main__':
    main()
