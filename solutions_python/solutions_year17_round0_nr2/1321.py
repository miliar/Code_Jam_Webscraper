def is_tidy(num):
    s = list(str(num))
    t = list(sorted(s))
    return s == t

T = int(raw_input())
for t in range(1, T + 1):
    N = int(raw_input())
    for j in range(N, 0, -1):
        if is_tidy(j):
            print 'Case #%d: %d' % (t, j)
            break
