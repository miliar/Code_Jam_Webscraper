def tidy(x):
    l = str(x)
    k = ""
    for c in l:
        nc = c
        if k and nc < k[-1]:
            nc = k[-1]
        k += nc
    return int(k)
    
T = int(raw_input())
for t in xrange(T):
    f = raw_input().split()
    l = list(f[0])
    s = int(f[1])
    n = 0
    for i in xrange(len(l)):
        if i+s > len(l):
            break
        if l[i] == "-":
            n += 1
            for j in xrange(s):
                if l[i+j] == "-":
                    l[i+j] = "+"
                else:
                    l[i+j] = "-"
    if l == list("+" * len(l)):
        print "Case #%d: %d" % (t+1, n)
    else:
        print "Case #%d: IMPOSSIBLE" % (t+1)
