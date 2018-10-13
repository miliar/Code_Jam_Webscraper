import sys

t = int(sys.stdin.readline().strip())
for ti in xrange(t):
    n = sys.stdin.readline().strip()
    n_len = len(n)
    n_lst = []
    for i in xrange(n_len):
        n_lst.append(int(n[i]))
    to_dec = 0
    for i in xrange(1, n_len):
        if n_lst[i] > n_lst[i - 1]:
            to_dec = i
            continue
        if n_lst[i] < n_lst[i - 1]:
            n_lst[to_dec] -= 1
            for j in xrange(to_dec + 1, n_len):
                n_lst[j] = 9
            break

    r = 0
    for i in n_lst:
        r = r * 10 + i

    print 'Case #%d: %d' % (ti + 1, r)
        
