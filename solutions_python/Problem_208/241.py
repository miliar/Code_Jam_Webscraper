tcc = int(raw_input().strip())
for inpo in range(1, tcc + 1):
    kol, q = map(int, raw_input().split())
    arr = []
    stump = []
    for i in range(kol):
        x, y = map(int, raw_input().split())
        arr.append(x)
        stump.append(y)
    d = [0]
    for i in range(kol):
        x = map(int, raw_input().split())
        if i < kol - 1:
            d.append(x[i + 1])
    for i in range(1, kol):
        d[i] += d[i - 1]
    for i in range(q):
        raw_input()
    __ = [0]
    for i in range(1, kol):
        tcc = None
        for j in range(i - 1, -1, -1):
            if d[i] - d[j] > arr[j]:
                continue
            t2 = __[j] + (d[i] - d[j]) / float(stump[j])
            if tcc is None or t2 < tcc:
                tcc = t2
        __.append(tcc)
    print("Case #%d: %.9lf" % (inpo, __[kol - 1]))
