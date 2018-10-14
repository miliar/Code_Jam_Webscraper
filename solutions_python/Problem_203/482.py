

t = int(raw_input())

for i in xrange(1, t + 1):
    r, c = map(int, raw_input().strip().split(" "))
    m = []
    for _r in xrange(r):
        m.append([0] * c)
        _input = list(raw_input())
        for _c in xrange(c):
            m[_r][_c] = _input[_c] if _input[_c] != "?" else 0

    empty_rows = []
    first_r_occur = None
    for _r in xrange(r):
        curr = 0
        first_ocurr = 0
        for _c in xrange(c):
            if m[_r][_c]:
                curr = m[_r][_c]
                if not first_ocurr:
                    first_ocurr = curr
            elif curr:
                m[_r][_c] = curr

        if not first_ocurr:
            empty_rows.append(_r)
        else:
            if first_r_occur is None:
                first_r_occur = _r
            for _c in xrange(c):
                if m[_r][_c]:
                    break
                else:
                    m[_r][_c] = first_ocurr

    while empty_rows:
        erow = empty_rows[0]
        if erow == 0:
            for _c in xrange(c):
                m[erow][_c] = m[first_r_occur][_c]
        else:
            for _c in xrange(c):
                m[erow][_c] = m[erow - 1][_c]
        del empty_rows[0]

    print "Case #{}:".format(i)
    for _r in xrange(r):
        print "".join(m[_r])
