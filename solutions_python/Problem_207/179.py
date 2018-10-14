import sys
import math


def small_pattern(counts, R, B, Y):
    if R >= B and R >= Y:
        cur = 'R'
        o1 = 'B'
        o2 = 'Y'
    elif B >= R and B >= Y:
        cur = 'B'
        o1 = 'R'
        o2 = 'Y'
    else:
        cur = 'Y'
        o1 = 'B'
        o2 = 'R'
    extra = counts[o1] + counts[o2] - counts[cur]
    res = []
    for i in xrange(extra):
        res.append(cur)
        res.append(o1)
        res.append(o2)
    for i in xrange(counts[o1] - extra):
        res.append(cur)
        res.append(o1)
    for i in xrange(counts[o2] - extra):
        res.append(cur)
        res.append(o2)
    return res


def evaluate(counts, N, target, ref):
    T = counts[target]
    REF = counts[ref]
    if T == 0:
        return ref, False
    if N > T + REF:
        if REF <= T:
            return "IMPOSSIBLE", True
        else:
            string = ((ref + target) * T) + ref
            counts[ref] -= T
            return string, False
    elif T != REF:
        return "IMPOSSIBLE", True
    else:
        return (ref + target) * T, True

with open("../files/" + '20172B'[-1] + "-large.in", 'r') as inp, open(
                    "../files/output" + '20172B'[-1] + ".txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i + 1) + ": {}"
        N, R, O, Y, G, B, V = map(int, inp.readline().split())
        counts = {'R': R, 'B': B, 'G': G, 'Y': Y, 'O': O, 'V': V}
        RG, final = evaluate(counts, N, 'G', 'R')
        if final:
            out.write(string.format(RG) + "\n")
            continue
        BO, final = evaluate(counts, N, 'O', 'B')
        if final:
            out.write(string.format(BO) + "\n")
            continue
        YV, final = evaluate(counts, N, 'V', 'Y')
        if final:
            out.write(string.format(YV) + "\n")
            continue
        R, B, Y = counts['R'], counts['B'], counts['Y']
        if R > Y + B or Y > R + B or B > R + Y:
            out.write(string.format("IMPOSSIBLE") + "\n")
            continue
        res = small_pattern(counts, R, B, Y)
        if B > 0:
            i = res.index('B')
            res[i] = BO
        if R > 0:
            i = res.index('R')
            res[i] = RG
        if Y > 0:
            i = res.index('Y')
            res[i] = YV
        out.write(string.format("".join(res)) + "\n")
