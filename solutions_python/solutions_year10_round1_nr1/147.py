T = int(raw_input(""))
for case in xrange(T):
    n, k = [int(x) for x in raw_input("").split()]
    old = [[0]*n for x in xrange(n)]
    new = [[0]*n for x in xrange(n)]
    for row in xrange(n):
        old[row] = list(raw_input(""))
    for r in xrange(n):
        for c in xrange(n):
            new[r][c] = old[n-c-1][r]
    for r in xrange(n-1,-1,-1):
        for c in xrange(n):
            if new[r][c] == '.':
                for r2 in xrange(r-1, -1, -1):
                    if new[r2][c] != '.':
                        new[r][c], new[r2][c] = new[r2][c], new[r][c]
                        break
    Rwin, Bwin = 0, 0
    for x in xrange(n):
        for i in xrange(n-k+1):
            if new[x][i:i+k] == ['B' for t in xrange(k)]:
                Bwin = 1
            if new[x][i:i+k] == ['R' for t in xrange(k)]:
                Rwin = 1
            if [temp[x] for temp in new[i:i+k]] == ['B' for t in xrange(k)]:
                Bwin = 1
            if [temp[x] for temp in new[i:i+k]] == ['R' for t in xrange(k)]:
                Rwin = 1
    for x in xrange(n-k+1):
        for i in xrange(n-k+1):
            if [new[x+t][i+t] for t in xrange(k)] == ['B' for t in xrange(k)]:
                Bwin = 1
            if [new[x+t][i+t] for t in xrange(k)] == ['R' for t in xrange(k)]:
                Rwin = 1
    for x in xrange(n-k+1):
        for i in xrange(k-1, n):
            if [new[x+t][i-t] for t in xrange(k)] == ['B' for t in xrange(k)]:
                Bwin = 1
            if [new[x+t][i-t] for t in xrange(k)] == ['R' for t in xrange(k)]:
                Rwin = 1
    if Rwin == 1 and Bwin == 0:
        winner = "Red"
    elif Rwin == 0 and Bwin == 1:
        winner = "Blue"
    elif Rwin == 1 and Bwin == 1:
        winner = "Both"
    elif Rwin == 0 and Bwin == 0:
        winner = "Neither"
    else:
        superfail()
    print "Case #%s: %s" %(case+1, winner)
