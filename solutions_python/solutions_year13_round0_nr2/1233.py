numcases = int(raw_input())

for case in xrange(numcases):
    height, width = tuple(map(int, raw_input().split()))
    grass = [map(int, raw_input().split()) for x in xrange(height)]
    rows = [max(x) for x in grass]
    cols = [max([grass[i][j] for i in xrange(height)]) for j in xrange(width)]
    failed = False
    for row in xrange(height):
        for col in xrange(width):
            if grass[row][col] != min([rows[row], cols[col]]):
                failed = True
                break
        if failed:
            break
    print "Case #%d: %s" % (case+1, "NO" if failed else "YES")