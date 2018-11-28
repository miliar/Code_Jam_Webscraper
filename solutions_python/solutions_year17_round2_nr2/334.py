from operator import itemgetter

def solve():
    n, r, o, y, g, b, v = map(int, input().split())
    colors = [('R', r), ('Y', y), ('B', b)]
    colors.sort(key=itemgetter(1), reverse=True)

    if colors[0][1] > n / 2:
        return 'IMPOSSIBLE'
    s = [colors[0][0]] * colors[0][1]

    l = len(s)
    i = 1
    for _ in range(colors[1][1]):
        s.insert(i, colors[1][0])
        i += 2
        l += 1

    for _ in range(colors[2][1]):
        if i > l:
            i = 1
        s.insert(i, colors[2][0])
        i += 2
        l += 1

    return ''.join(s)

t = int(input())
for i in range(t):
    print('Case #%d: %s' % (i + 1, solve()))