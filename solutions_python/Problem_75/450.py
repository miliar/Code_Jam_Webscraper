import os
import os.path

base = "QWERASDF"

def solve(combs, anni, invoke):
    combine = {}
    for i in base:
        combine[i] = {}
        for j in base:
            combine[i][j] = None

    for c in combs:
        a,b,t = c
        combine[a][b] = t
        combine[b][a] = t

    oppose = {}
    for i in base:
        oppose[i] = []
    for a in anni:
        g,h = a
        oppose[g].append(h)
        oppose[h].append(g)

    el_list = [invoke[0]]
    pos = 1
    length = len(invoke)

    while pos < length:
        el_list.append(invoke[pos])
        if len(el_list) < 2:
            pos += 1
            continue

        if el_list[-1] in base and el_list[-2] in base:
            com = combine[el_list[-1]][el_list[-2]]
            if com:
                el_list = el_list[:-2]
                el_list.append(com)

        if el_list[-1] in base:
            opp = oppose[el_list[-1]]
            for t in opp:
                if t in el_list[:-1]:
                    el_list = []
                    break

        pos += 1
    return el_list

def magicka(path):
    fin = open(path)
    out_path = os.path.splitext(path)[0] + ".sol"
    fout = open(out_path, "w")

    num_cases = int(fin.readline().strip())

    for i in range(num_cases):
        prob = fin.readline().strip().split()
        num_coms = int(prob.pop(0))
        combine = []
        for j in range(num_coms):
            combine.append(prob.pop(0))
        oppose = []
        num_opps = int(prob.pop(0))
        for j in range(num_opps):
            oppose.append(prob.pop(0))
        length = int(prob.pop(0))
        invoke = prob.pop(0)
        sol = solve(combine, oppose, invoke)
        fout.write("Case #%i: %s\n" %(i+1, repr(sol).replace("'", "")))

    fout.close()
    fin.close()
