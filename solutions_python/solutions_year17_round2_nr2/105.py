#!/usr/bin/env python

num_tests = input()

for test_no in xrange(1, num_tests + 1):
    N, R, O, Y, G, B, V = map(int, raw_input().split())
    counts = [[R, 'R'], [Y, 'Y'], [B, 'B']]
    counts.sort(reverse=True)
    if counts[0][0] > counts[1][0] + counts[2][0]:
        print 'Case #{0}: IMPOSSIBLE'.format(test_no)
        continue

    sol = [counts[0][1]]
    counts[0][0] -= 1
    for i in xrange(1, N):
        counts.sort(reverse=True)
        c = [tup for tup in counts if tup[1] != sol[-1]]
        if c[0][0] > c[1][0]:
            sol.append(c[0][1])
            c[0][0] -= 1
        elif c[0][0] == c[1][0] and c[0][1] == sol[0]:
            sol.append(c[0][1])
            c[0][0] -= 1
        else:
            sol.append(c[1][1])
            c[1][0] -= 1

    
    print 'Case #{0}: {1}'.format(test_no, ''.join(sol))
