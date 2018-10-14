cases = int(raw_input())

for case in xrange(cases):
    height, width = map(int, raw_input().split())
    
    h_max = [0]*height
    v_max = [0]*width
    lawn = []

    for r in xrange(height):
        row = map(int, raw_input().split())
        lawn.append(row)
        h_max[r] = max(row)
        for c in xrange(width):
            if row[c] > v_max[c]:
                v_max[c] = row[c]

    possible = True
    for r in xrange(height):
        if not possible:
            break
        for c in xrange(width):
            current = lawn[r][c]
            if h_max[r] > current and v_max[c] > current:
                possible = False
                break

    print 'Case #%d: %s' % (case+1, 'YES' if possible else 'NO')
    # if there exists a max > current square in both hor and ver dirs, naht possible
