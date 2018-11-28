def solve(cakes, k):
    cakes = list(cakes)
    cnt = 0
    for i in range(len(cakes) - k + 1):
        if cakes[i] == '-':
            cnt += 1
            for c in range(i, i + k):
                if cakes[c] == '-':
                    cakes[c] = '+'
                else:
                    cakes[c] = '-'
    for cake in cakes:
        if cake != '+':
            return False, 0
    return True, cnt

T = int(input().strip())

f = open('panres.txt', 'w')

for C in range(1, T + 1):
    x = input().strip()
    cake, k = x.split(' ')
    k = int(k)
    b, s = solve(cake, k)
    if b:
        f.write('Case #{0}: {1}\n'.format(C, s))
    else:
        f.write('Case #{0}: IMPOSSIBLE\n'.format(C))
f.close()
        
