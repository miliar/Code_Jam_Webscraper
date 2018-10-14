T = int(raw_input())
for t in xrange(1, T + 1):
    N = map(int, raw_input())

    tidy = N[:]
    was_error = False

    i = 1
    for i in xrange(1, len(N)):
        if tidy[i] < tidy[i - 1]:
            was_error = True
            break

    if was_error:
        j = i - 1
        for j in xrange(i - 1, -1, -1):
            tidy[j] -= 1
            if j == 0:
                break
            if tidy[j] >= tidy[j - 1]:
                break

        for k in xrange(j + 1, len(N)):
            tidy[k] = 9

    print 'Case #{}: {}'.format(t, int(''.join(map(str, tidy))))
