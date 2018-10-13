#! /usr/bin/python3

T = int(input())
for t in range(1, T+1):
    [cakes, flipper] = input().split(' ')
    flipper = int(flipper)
    cakes = [x for x in cakes]
    i = 0
    L = len(cakes)
    r = 0
    while i < L:
        if cakes[i] == '+':
            i += 1
            continue
        if i + flipper > L:
            r = 'IMPOSSIBLE'
            break
        for j in range(flipper):
            if cakes[i+j] == '-':
                cakes[i+j] = '+'
            else:
                cakes[i+j] = '-'
        r += 1
        i += 1
    r = str(r)
    print('Case #%d: %s' % (t, r))