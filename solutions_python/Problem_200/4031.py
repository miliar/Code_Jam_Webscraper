N = int(raw_input())


def is_tidy(n):
    check = True
    last = 0
    n_list = map(int, str(n))
    for idx, i in enumerate(n_list):
        j = i
        if j < last:
            check = False
            break
        last = j
    if check:
        return n
    else:
        idx -= 1
        n_list_new = None
        while idx > 0:
            if n_list[idx] - 1 >= n_list[idx - 1]:
                n_list_new = n_list[0:idx] + [n_list[idx] -
                                              1] + [9] * (len(n_list) - idx - 1)
                break
            idx -= 1
        if idx == 0:
            n_list_new = [n_list[0] - 1] + [9] * (len(n_list) - 1)
        return int(''.join(map(str, n_list_new)))

for case in xrange(N):
    n = int(raw_input())
    print "Case #%d: %d" % (case + 1, is_tidy(n))
