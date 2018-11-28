def n_flips(pks, k):
    l = len(pks)
    flips = 0
    for i in xrange(l):
        p = pks[i]
        if p == '-':
            if i + k > l:
                return 'IMPOSSIBLE'
            else:
                flips += 1
                for j in xrange(k):
                    pks[j+i] = '+' if pks[j+i] == '-' else '-'
    return flips

N = int(raw_input())
for I in xrange(N):
    pks, k = raw_input().split()
    c = I + 1
    print('Case #{}: {}'.format(c, n_flips(list(pks), int(k))))
