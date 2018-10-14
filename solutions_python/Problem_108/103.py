import sys

T = int(sys.stdin.readline())

for i in xrange(T):
    N = int(sys.stdin.readline())

    vines = []
    for j in xrange(N):
        vines.append(sys.stdin.readline().split())

    vines = map(lambda x: (int(x[0]), int(x[1])), vines)
    D = int(sys.stdin.readline())

    potential = set()
    potential.add((vines[0], vines[0][0]))

    possible = False
    while len(potential) > 0:
        #print potential
        vine = potential.pop()
        if vine[0][0] + vine[1] >= D:
            possible = True
            break
        for v in vines:
            if v[0] <= vine[0][0]:
                #print "Skipping vine because %d < %d" % (v[0], vine[0][0])
                continue
            if vine[0][0] + vine[1] >= v[0]:
                #print "Can swing from point %d with length %d to reach point %d" % (vine[0][0], vine[1], v[0])
                potential.add((v, min(v[1], v[0] - vine[0][0])))

    if possible:
        print "Case #%d: YES" % (i+1)
    else:
        print "Case #%d: NO" % (i+1)



