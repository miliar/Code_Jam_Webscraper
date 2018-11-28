def last_tidy(n):
    digs = [int(d) for d in str(n)]
    while digs != sorted(digs):
        for i in range(len(digs)-1):
            if digs[i] > digs[i+1]:
                digs[i] -= 1
                digs[i+1:] = [9]*(len(digs)-i-1)
                break
    return int(''.join(map(str, digs)))

T = int(input())
for i in range(T):
    N = int(input())
    print('Case #%d: %d' % (i+1, last_tidy(N)))
