from sys import stdin

for i in xrange(1, 1+int(stdin.readline())):
    N = int(stdin.readline())
    vines = []
    for n in xrange(N):
        vines.append(tuple(map(int, stdin.readline().split())))
    love = int(stdin.readline())
    vines.sort(key=lambda x: x[0])
    Q = [(0,min(vines[0][0],vines[0][1]))]
    result = "NO"
    done = {}
    while Q:
        frm, swing = Q.pop()
        done[frm,swing] = 1
        if vines[frm][0] + swing >= love:
            result = "YES"
            break
        for j in xrange(frm+1, N):
            if vines[frm][0] + swing >= vines[j][0]:
                if vines[j][1] + vines[frm][0] < vines[j][0]:
                    o = (j,vines[j][1])
                else:
                    o = (j,vines[j][0]-vines[frm][0])
                if o not in done:
                    Q.append(o)
    print "Case #%d: %s" % (i, result)
