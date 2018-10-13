lawn = []

testnum = int(raw_input())

for test in range(testnum):
    nrow, ncol = map(int,raw_input().split(" "))

    row = [map(int,raw_input().split(" ")) for _ in range(nrow)]
    col = []
    for i in range(ncol):
        col.append([l[i] for l in row])

    rowmax = [reduce(max,r) for r in row]
    colmax = [reduce(max,c) for c in col]

    can = 1
    for i in range(nrow):
        if can == 0:
            break
        for j in range(ncol):
            if row[i][j] < rowmax[i] and row[i][j] < colmax[j]:
                can = 0
                break

    if can:
        print "Case #%d: YES" % (test+1)
    else:
        print "Case #%d: NO" % (test+1)