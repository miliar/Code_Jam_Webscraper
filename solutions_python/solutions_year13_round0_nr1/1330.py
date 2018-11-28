n = input()

player = ''

def ch(c):
    global player
    if c == 'T':
        return player
    return c

for test in xrange(n):
    f = [raw_input() for _ in xrange(4)]
    lines = f 
    lines.append(reduce(lambda x, y: x+y, [f[i][i] for i in xrange(4)], ''))
    lines.append(reduce(lambda x, y: x+y, [f[i][3-i] for i in xrange(4)],''))
    for i in xrange(4):
        lines.append(reduce(lambda x, y: x+y, [f[j][i] for j in xrange(4)], ''))
    ans = 'Draw'
    for i in f:
        for j in i:
            if j == '.':
                ans = 'Game has not completed'
    for v in ['X', 'O']:
        t = list(lines)
        player = v
        for x in xrange(10):
            t[x] = map(ch, t[x])
        lv = [v]*4
        if lv in t:
            ans = v + ' won'
    print 'Case #%d: %s' % (test+1, ans)
    try:
        raw_input()
    except:
        break
