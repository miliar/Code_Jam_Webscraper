
def flipper(cakes, n):
    l = len(cakes)
    ret = 0
    for i in range(l-n + 1):
        if not cakes[i] == '-':
            continue
        for x in range(i, i+n):
            if cakes[x] == '-':
                cakes[x] = '+'
            else:
                cakes[x] = '-'
        ret += 1
    if '-' in cakes[-n:]:
        return None
    return ret


def main():
    t = int(raw_input().strip())
    for i in xrange(t):
        cakes, n = raw_input().strip().split()
        n = int(n)
        ans = flipper(list(cakes), n)
        print "Case #%s: %s" % (i + 1, ans if ans is not None else "IMPOSSIBLE")

if __name__ == '__main__':
    main()