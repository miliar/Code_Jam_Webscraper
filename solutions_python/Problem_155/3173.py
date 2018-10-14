f = open('input.in')
f.readline()

case = 1
for row in f.readlines():
    s_max, s = row.split()
    s_max = int(s_max)
    ss = [int(e) for e in s]

    n = 0
    k = 0
    s = 0
    for s_k in ss:
        if s < k:
            n = n + 1
            s = k

        k = k + 1

        s += s_k

    print "Case #{}: {}".format(case, n)
    case += 1
