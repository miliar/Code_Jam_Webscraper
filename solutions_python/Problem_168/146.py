T = int(raw_input().strip())


NO, LEFT, RIGHT, DOWN, UP = range(5)
charmap = [".", "<", ">", "v", "^"]


def convert(chars):
    ret = [0 for i in xrange(len(chars))]

    for i, char in enumerate(chars):
        for j, pos in enumerate(charmap):
            if char == pos:
                ret[i] = j
                break

    return ret


def has(rectangle, r, c, direction):
    ret = False
    if direction == LEFT:
        curr = c - 1
        while curr > -1:
            if rectangle[r][curr] != NO:
                ret = True
                break
            curr -= 1
    elif direction == RIGHT:
        curr = c + 1
        while curr < len(rectangle[0]):
            if rectangle[r][curr] != NO:
                ret = True
                break
            curr += 1
    elif direction == DOWN:
        curr = r + 1
        while curr < len(rectangle):
            if rectangle[curr][c] != NO:
                ret = True
                break
            curr += 1
    else:  # direction == UP
        curr = r - 1
        while curr > -1:
            if rectangle[curr][c] != NO:
                ret = True
                break
            curr -= 1

    return ret

for i in xrange(1, T + 1):
    R, C = map(int, raw_input().strip().split())
    rectangle = [[NO for _ in xrange(C)] for _2 in xrange(R)]
    for j in xrange(R):
        rectangle[j] = convert(raw_input().strip())

    imp = False
    total = 0
    for r in xrange(R):
        for c in xrange(C):
            direction = rectangle[r][c]
            if direction == NO or has(rectangle, r, c, direction):
                continue
            if any([has(rectangle, r, c, cdir) for cdir in (LEFT, RIGHT, DOWN, UP)]):
                total += 1
            else:
                imp = True
                break
        if imp:
            break

    if imp:
        print "Case #%s: IMPOSSIBLE" % (i, )
    else:
        print "Case #%s: %s" % (i, total)
