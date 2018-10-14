def is_tidy(n):
    t = str(n)
    return all(i <= j for i, j in zip(t[:-1], t[1:]))


def tidy(n):
    t = str(n)
    l = len(t)
    for idx in range(l):
        if idx < l-1 and t[idx] > t[idx + 1]:
            n = int(str(tidy(int(t[:idx+1]) - 1)) + '9' * (l - idx-1))
            break
    while not is_tidy(n):
        n -= 1
    return n


def main():
    t = int(raw_input().strip())
    for i in xrange(t):
        n = int(raw_input().strip())
        ans = tidy(n)
        print "Case #%s: %s" % (i + 1, ans)

if __name__ == '__main__':
    main()
