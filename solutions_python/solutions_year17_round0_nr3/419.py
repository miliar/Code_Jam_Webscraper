def empty_stalls(N, K):
    max_s = N / 2
    min_s = (max_s - 1) if (N % 2 == 0) else max_s

    if K == 1:
        return (max_s, min_s)
    else:
        chosen_s = max_s if (K % 2 == 0) else min_s
        return empty_stalls(chosen_s, K / 2)


def main():
    # print empty_stalls(4, 2)
    # print empty_stalls(5, 2)
    # print empty_stalls(6, 2)
    # print empty_stalls(1000, 1000)
    # print empty_stalls(1000, 1)

    t = int(raw_input())
    for i in xrange(1, t + 1):
        N, K = raw_input().split(' ')
        max_s, min_s = empty_stalls(int(N), int(K))
        print 'Case #%d: %d %d' % (i, max_s, min_s)

if __name__ == '__main__':
    main()
