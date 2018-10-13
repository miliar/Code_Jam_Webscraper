
def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret


def main():
    for t in range(1, 1+input()):
        D = input()
        P = read_array(int)
        best_ans = max(P)
        for max_allow in range(1, max(P)):
            cut = 0
            for p in P:
                cut += (p - 1) / max_allow
            ans = cut + max_allow
            best_ans = min(best_ans, ans)

        print 'Case #%d: %d' % (t, best_ans)


main()
