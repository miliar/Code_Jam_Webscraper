for _ in xrange(input()):
    print "Case #%d:" % (_+1)
    r, c = map(int, raw_input().split())
    Cake = [list(raw_input()) for i in xrange(r)]
    used = set()
    for i in xrange(r):
        for j in xrange(c):
            ch = Cake[i][j]
            if ch != '?' and ch not in used:
                used.add(ch)
                dx = 1
                while j+dx < c and Cake[i][j+dx] == '?':
                    Cake[i][j+dx] = ch
                    dx += 1
                dx = -1
                while j+dx > -1 and Cake[i][j+dx] == '?':
                    Cake[i][j+dx] = ch
                    dx -= 1
    for i in xrange(r):
        if Cake[i][0] != '?':
            dy = 1
            while i+dy < r and Cake[i+dy][0] == '?':
                Cake[i+dy] = Cake[i]
                dy += 1
            dy = -1
            while i+dy > -1 and Cake[i+dy][0] == '?':
                Cake[i+dy] = Cake[i]
                dy -= 1
    print '\n'.join("".join(line) for line in Cake)
