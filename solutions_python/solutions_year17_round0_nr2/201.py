def last_tidy(N):
    N = str(N)
    was_tidy = True

    for i in xrange(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            was_tidy = False
            N = N[:i+1] + '0'*(len(N)-i-1)
            break
    if was_tidy:
        return int(N)
    else:
        return last_tidy(int(N)-1)

t = int(raw_input())

for x in xrange(1, t+1):
    print 'Case #{}: {}'.format(x, last_tidy(raw_input()))