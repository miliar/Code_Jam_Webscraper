def check(pic, x, y):
    try:
        return pic[x][y] == '#' and pic[x+1][y+1] == '#' and pic[x+1][y] == '#' and pic[x][y+1] == '#'
    except:
        pass
    return False

for case in xrange(int(raw_input())):
    R, C = map(int, raw_input().split())
    pic = [[y for y in raw_input()] for x in xrange(R)]
    impossible = False
    for r in xrange(R):
        for c in xrange(C):
            if pic[r][c] == '#':
                if not check(pic, r, c):
                    impossible = True
                    break
                pic[r][c] = '/'
                pic[r+1][c] = '\\'
                pic[r+1][c+1] = '/'
                pic[r][c+1] = '\\'

        if impossible:
            break

    print 'Case #%d: ' % (case+1)
    if impossible:
        print 'Impossible'
    else:
        for r in xrange(R):
            print ''.join(pic[r])
