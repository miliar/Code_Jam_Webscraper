def solve(smax, s):
    if smax==0:
        return 0
    level = range(smax+1)
    extra, current = 0, 0
    for l in level:
        if current < l:
            add = l-current
            extra += add
            current += add
        current += s[l]
    return extra


with open('A-large.in', 'r') as file:
    f = [l.strip() for l in file.readlines()]
    T = int(f.pop(0))
    for t in range(T):
        sd = f[t].split(' ')
        smax, s = int(sd[0]), map(int, list(sd[1]))
        extra = solve(smax, s)
        print "Case #%d: %d" % (t+1, extra)