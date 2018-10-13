def lottery(A, B, K):
    count = 0
    for i in xrange(A):
        for j in xrange(B):
            if i & j < K:
                count += 1
    return count

if __name__ == '__main__':
    T = input()

    for case in xrange(T):
        A, B, K = [int(x) for x in raw_input().split()]

        print 'Case #%d: %d' % (case+1, lottery(A, B, K))