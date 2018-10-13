#!/usr/bin/python

with open('input.txt', 'r') as inp:
    cases = int(inp.readline())
    case_no = 1

    for case in range(0, cases):

        blocks_count = int(inp.readline())

        b_N = [float(l.strip()) for l in inp.readline().split(' ')]
        b_K = [float(l.strip()) for l in inp.readline().split(' ')]

        points = [0, 0]

        t_N = list(b_N)
        t_K = list(b_K)

        while t_N:
            max_N = max(t_N)
            min_N = min(t_N)
            max_K = max(t_K)
            min_K = min(t_K)

            if max_N > max_K:
                points[0] += 1
                t_N.remove(max_N)
                t_K.remove(max_K)
            else:
                t_N.remove(min_N)
                t_K.remove(max_K)

        while b_N:

            block_n = min(b_N)

            try:
                block_k = min([value for value in b_K if value >= block_n])
            except:
                block_k = min(b_K)

            if (block_n > block_k):
                points[1] += 1

            b_N.remove(block_n)
            b_K.remove(block_k)

        print "Case #%d: %d %d" % (case_no, points[0], points[1])
        case_no += 1

