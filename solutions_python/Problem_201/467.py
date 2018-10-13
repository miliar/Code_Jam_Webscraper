for i in xrange(0, int(raw_input())):
    n, k = map(int, raw_input().split())
    a = n
    b = 0
    aCount = 1
    bCount = 0
    end = 1
    while True:
        if k <= end:
            val = 0
            if k <= aCount:
                val = a
            else:
                val = b
            print "Case #%d: %d %d"%(i+1, val/2, val - (val/2) -1)
            break
        k -= end
        end *= 2

        s = set()
        s.add(a/2)
        s.add(a - (a/2) - 1)
        if b > 0:
            s.add(b/2)
            s.add(b - (b/2) - 1)

        l = list(s)
        l.sort(reverse=True)

        if len(l) == 1:
            l.append(0)

        ac = 0
        bc = 0
        if a/2 == l[0]:
            ac += aCount
        else:
            bc += aCount
        if a - (a/2) - 1 == l[0]:
            ac += aCount
        else:
            bc += aCount
        if b/2 == l[0]:
            ac += bCount
        else:
            bc += bCount
        if b - (b/2) - 1 == l[0]:
            ac += bCount
        else:
            bc += bCount

        a = l[0]
        b = l[1]
        aCount = ac
        bCount = bc
