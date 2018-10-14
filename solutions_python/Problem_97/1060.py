if __name__ == "__main__":
    fin = open("C-small-attempt0.in", "r")
    fout = open("C-small-attempt0.out", "w")
    T = int(fin.readline())
    for cas in range(T):
        l = fin.readline().strip().split()
        f, r = map(int, l)
        ans = 0
        bbs = 0
        cache = set()
        for val in xrange(f, r + 1):
            pre = str(val)
            for i in range(len(pre)):
                next = pre[i:] + pre[:i]
                if not next.startswith('0') and next != pre and (int(next) >= f and  int(next) <= r):
                    if (pre, next) not in cache:
                        ans += 1
                    cache.add((pre, next))
        ans /= 2
        print  >> fout, ("Case #%d: %s" % (cas + 1, ans))
