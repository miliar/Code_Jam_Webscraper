import sys
sys.setrecursionlimit(10005)


def calc(dep, C, F, X, v):
    if C / v >= X / v or dep >= 10000:
        return X / v
    return min(X / v, calc(dep + 1, C, F, X, v + F) + C / v)


def main():
    num_of_tests = int(raw_input())
    a = [0 for i in range(4)]
    for test_i in range(num_of_tests):
        C, F, X = map(float, raw_input().split())
        ans = calc(0, C, F, X, 2.0)
        print "Case #%d: %s" % (test_i + 1, ans)


if __name__ == "__main__":
    main()
