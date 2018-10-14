def nxt(m, current, first):
    mx = 0.0
    selection = None
    for k in m.keys():
        if k == current:
            continue
        score = float(m[k])
        if k == first:
            score = score + 0.5
        if score > mx:
            mx = m[k]
            selection = k
    return selection


with open('input.txt') as inp:
    with open('output.txt', 'w') as outp:
        ncases = int(inp.readline().strip())
        for nc in range(0, ncases):
            N, R, O, Y, G, B, V = inp.readline().strip().split(' ')
            m = {'R':int(R), 'O':int(O), 'Y':int(Y), 'G':int(G), 'B':int(B), 'V':int(V)}
            is_impossible = False
            for k in m.keys():
                if m[k] > int(N) / 2:
                    is_impossible = True
            if is_impossible:
                outp.write("Case #{}: IMPOSSIBLE\n".format(nc + 1))
                continue
            s = ''
            sel = ''
            first = None
            for i in xrange(0, int(N)):
                sel = nxt(m, sel, first)
                s = s + sel
                m[sel] = m[sel] - 1
                if first == None:
                    first = sel
            outp.write("Case #{}: {}\n".format(nc + 1, s))
