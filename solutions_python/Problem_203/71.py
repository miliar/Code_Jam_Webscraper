#
def solve(M, N, cake):
    for i in cake:
        print i
    firstline = -1
    for i in range(M):
        for j in range(N):
            if cake[i][j] != '?':
                firstline = i
                break
        if firstline >= 0:
            break
    firstline = max(firstline, 0)
    # print "firstline", firstline
    for i in range(firstline, M):
        cur = ""
        for j in range(N):
            if cake[i][j] != '?':
                cur = cake[i][j]
                break
        if cur == "":
            cake[i][:] = cake[i - 1][:]
            continue
        for j in range(N):
            if cake[i][j] == '?':
                cake[i][j] = cur
            else:
                cur = cake[i][j]
    for i in range(firstline):
        cake[i][:] = cake[firstline][:]
    cake = [''.join(i) for i in cake]
    return '\n'.join(cake)

fi = open('A-large.in', 'r')
fo = open('A-large.out', 'w')
T = int(fi.readline().strip())
for i in xrange(T):
    M, N = map(int, fi.readline().strip().split())
    cake = []
    for _ in range(M):
        cake.append(list(fi.readline().strip()))
    res = solve(M, N, cake)
    out = "Case #%d:\n%s\n" % (i + 1, res)
    print N, M, out
    fo.write(out)
fi.close()
fo.close()

# print solve(2, 3, [['?', '?', 'C'], ['B', 'A', '?']])
