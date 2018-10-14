def f():
    n, r, o, y, g, b, v = map(int, input().split())
    if n % 2 == 0:
        if r == n // 2 and g == n // 2:
            return 'RG' * (n // 2)
        elif y == n // 2 and v == n // 2:
            return 'YV' * (n // 2)
        elif b == n // 2 and o == n // 2:
            return 'BO' * (n // 2)
    if o:
        if b <= o:
            return 'IMPOSSIBLE'
        n -= 2 * o
        b -= o
    if g:
        if r <= g:
            return 'IMPOSSIBLE'
        n -= 2 * g
        r -= g
    if v:
        if y <= v:
            return 'IMPOSSIBLE'
        n -= 2 * v
        y -= v
    s = ''
    c = sorted(([r, 0], [y, 1], [b, 2]))
    for i in range(n):
        if i and c[1][0] == c[2][0] and 'RYB'[c[1][1]] == s[0]:
            c[1], c[2] = c[2], c[1]
        x = 2
        if i == 0 or 'RYB'[c[2][1]] != s[-1]:
            pass
        elif c[1][0] == 0:
            return 'IMPOSSIBLE'
        else:
            x = 1
        s = s + 'RYB'[c[x][1]]
        c[x][0] -= 1
        c.sort()
    if s[0] == s[-1]:
        return 'IMPOSSIBLE'
    if o:
        x = s.find('B')
        s = s[:x] + 'BO' * o + s[x:]
    if g:
        x = s.find('R')
        s = s[:x] + 'RG' * g + s[x:]
    if v:
        x = s.find('Y')
        s = s[:x] + 'YV' * v + s[x:]
    return s

for t in range(int(input())):
    print('Case #{}: {}'.format(t + 1, f()))
