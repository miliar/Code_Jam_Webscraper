# -*- coding: utf-8 -*-

T = int(raw_input())
for case in xrange(1, T + 1):
    N = int(raw_input())
    C = [int(x) for x in raw_input().split(' ')]
    C.sort()

    allxor = reduce(lambda a, b: a ^ b, C, 0)
    if allxor != 0:
        print 'Case #%d: NO' % case
        continue

    choice = 1
    while choice < 2 ** N - 1:
        def bin(n):
            r = []
            while 0 < n:
                r.append(n & 1 == 1)
                n >>= 1
            return r
        cl = bin(choice)
        if len(cl) < N:
            cl += [False] * (N - len(cl))
        Patric = [C[i] for i in xrange(N) if cl[i]]
        Sean = [C[i] for i in xrange(N) if not cl[i]]

        sum_Patric = reduce(lambda a, b: a ^ b, Patric)
        sum_Sean = reduce(lambda a, b: a ^ b, Sean)
        if sum_Patric == sum_Sean:
            print 'Case #%d: %d' % (case, sum(Sean))
            break
        
        choice += 1
    else:
        print 'Case #%d: NO' % case
