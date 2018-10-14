def spread_r(r, c, lines, dr):
    ch = lines[r][c]

    while r + dr >= 0 and r + dr < len(lines):
        r += dr
        if (lines[r][c] == '?'):
            lines[r][c] = ch
        else:
            break

    return lines


def spread_c(r, c, lines, dc):
    ch = lines[r][c]

    while c + dc >= 0 and c + dc < len(lines[0]):
        c += dc
        if (lines[r][c] == '?'):
            lines[r][c] = ch
        else:
            break

    return lines

def print_lines(lines):
    for l in lines:
        print ''.join(l)



t = int(raw_input())

for i in xrange(t):
    r, c = map(int, raw_input().split())
    
    lines = []
    for rr in xrange(r):
        line = raw_input()

        lines.append([])

        for cc in xrange(c):
            lines[rr].append(line[cc])


    for r in xrange(len(lines)):
        for c in xrange(len(lines[0])):
            if lines[r][c] != '?':
                lines = spread_r(r, c, lines, 1)
                lines = spread_r(r, c, lines, -1)

    for r in xrange(len(lines)):
        for c in xrange(len(lines[0])):
            if lines[r][c] != '?':
                lines = spread_c(r, c, lines, 1)
                lines = spread_c(r, c, lines, -1)
            # print
            # print_lines(lines)

    print 'Case #%d:' % (i + 1)
    print_lines(lines)