# coding: utf-8


def ok(ans, a):
    s = a[0]
    for i in range(1, len(a)):
        if s < i:
            return False
        s += a[i]
    return True


def work():
    m, a = raw_input().strip().split()
    m = int(m)
    a = map(int, a)
    l = 0
    r = m
    while l < r:
        mid = (l + r) / 2
        a[0] += mid
        if ok(mid, a):
            r = mid
        else:
            l = mid + 1
        a[0] -= mid
    return l


def main():
    n_testcase = int(raw_input())
    for case in range(1, n_testcase + 1):
        ans = work()
        print 'Case #%s: %s' % (case, ans)


if __name__ == "__main__":
    main()
