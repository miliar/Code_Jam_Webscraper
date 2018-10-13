for _ in xrange(input()):
    print "Case #%d:" % (_+1),
    n = raw_input()
    l = len(n)
    nn = map(int, n)

    def dfs(c, less, st):
        if c == l:
            return int(st)
        if less:
            v = dfs(c+1, 1, st + '9')
        else:
            v = 0
            if c == l-1 or nn[c] <= nn[c+1]:
                v = max(v, dfs(c+1, 0, st + n[c]))
            if c == 0 or nn[c-1] <= nn[c]-1:
                v = max(v, dfs(c+1, 1, st + str(nn[c]-1)))
        return v
    print dfs(0, 0, "")
