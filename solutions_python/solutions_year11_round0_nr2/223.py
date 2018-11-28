def calc_result(combines, opposed, order):
    comb = {}
    for i,j,k in combines:
        comb[i, j] = k
        comb[j, i] = k
    opp = {}
    for i,j in opposed:
        opp[i] = j
        opp[j] = i

    l = [None]
    for elem in order:
        if (elem, l[-1]) in comb:
            l[-1] = comb[elem, l[-1]]
        else:
            if elem in opp and opp[elem] in l:
                l = [None]
            else:
                l.append(elem)
    return l[1:]

def solve_B(infile, outfile):
    inputs = open(infile).readlines()[1:]
    R = []
    for i, inp in enumerate(inputs):
        vals = inp.split()
        C = int(vals[0])
        combines = vals[1:1+C]
        D = int(vals[1+C])
        opposed = vals[2+C:2+C+D]
        N = int(vals[2+C+D])
        order = vals[3+C+D]
        res = calc_result(combines, opposed, order)
        R.append("Case #%d: [%s]" % (i + 1, ", ".join(res)))
    open(outfile, "w").write("\n".join(R))
