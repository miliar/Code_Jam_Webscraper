
t = int(raw_input())

for ti in xrange(1, t + 1):
    inp = raw_input()
    n = []
    for sym in inp:
        n.append(int(sym))

    ln = len(n)
    if ln == 1:
        print "Case #{}: {}".format(ti, n[0])
        continue

    for el in xrange(ln - 1, 0, -1):
        if n[el - 1] > n[el]:
            n[el - 1] -= 1
            n = n[:el]
            n.extend([9] * (ln - el))

    while n[0] == 0:
        n = n[1:]
    print "Case #{}: {}".format(ti, "".join(map(str, n)))
