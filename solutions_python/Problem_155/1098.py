T = input()

for casenbr in range(T):
    Smax, ss = raw_input().split()
    Sis = [(idx, int(n)) for idx, n in enumerate(ss) if n != "0"]
    acc = 0
    ans = 0
    for idx, n in Sis:
        if acc >= idx:
            acc += n
            continue
        extra = idx - acc
        ans += extra
        acc += extra + n

    print "Case #%d: %s" % (casenbr+1, ans)
