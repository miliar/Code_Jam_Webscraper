cases = int(input())
flip = lambda x: ''.join('+' if c == '-' else '-' for c in x)
for c in range(cases):
    cakes, _k = input().strip().split()
    k = int(_k)
    flips = 0
    for i in range(len(cakes)-k+1):
        if cakes[i] == '-':
            cakes = cakes[:i] + flip(cakes[i:i+k]) + cakes[i+k:]
            flips += 1
    print('Case #%d:' % (c+1), end=' ')
    if cakes == ('+' * len(cakes)):
        print(flips)
    else:
        print('IMPOSSIBLE')

