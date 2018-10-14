f = open("A-large.in")
fout = open("A-large.out", "w")

def move(pos, target, n):
    if pos < target:
        return pos + min(abs(pos - target), n)
    else:
        return pos - min(abs(pos - target), n)


T = int(f.readline())
for t in xrange(T):
    v = f.readline().strip().split()
    
    order = []
    butt = {'B': [], 'O': []}
    pos = {'B': 1, 'O': 1}
    
    for i in xrange(int(v[0])):
        c, n = v[i*2+1], int(v[i*2+2])
        order.append(c)
        butt[c].append(n)

    # dummy
    butt['B'].append(-1)
    butt['O'].append(-1)

    result = 0
    for c in order:
        d = abs(pos[c] - butt[c][0])
        pos[c] = butt[c][0]
        del butt[c][0]

        other = 'B' if c == 'O' else 'O'
        pos[other] = move(pos[other], butt[other][0], d + 1)

        result += d + 1

    print >>fout, "Case #%d: %d" % (t+1, result)
