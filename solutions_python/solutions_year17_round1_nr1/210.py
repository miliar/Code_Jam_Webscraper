import sys

T = int(raw_input())

for t in range(1, T+1):
    R, C = map(int, raw_input().split())

    cakes = []
    firstline_qs = False
    for ri in range(R):
        cake = list(raw_input())
        # all '?'
        if len(filter(lambda x: x != '?', cake)) == 0:
            if ri == 0 or firstline_qs: 
                firstline_qs = True
                continue
            else: 
                cake = cakes[-1]

        if '?' in cake:
            qs = []
            initial = None
            for ci in range(C):
                if cake[ci] == '?' and initial:
                    cake[ci] = initial
                elif cake[ci] != '?':
                    initial = cake[ci]
                    if ci != 0 and cake[0] == '?':
                        for k in range(ci):
                            cake[k] = initial

        if firstline_qs:
            for k in range(ri):
                cakes.append(cake)
            firstline_qs = False
        cakes.append(cake)

    print 'Case #%d:' % (t)
    for ri in range(R):
        print ''.join(cakes[ri])
