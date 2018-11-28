def solve(int_ac, int_aj):
    tempo_ac = 720 - sum(ei - bi for bi, ei, cod in int_ac)
    assert tempo_ac >= 0, tempo_ac
    tempo_aj = 720 - sum(ei - bi for bi, ei, cod in int_aj)
    assert tempo_aj >= 0, tempo_aj
    # print 720 - tempo_ac, 720 - tempo_aj
    tot_int = sorted(int_ac + int_aj, key=lambda x: x[0])
    spazio_ac = []
    spazio_aj = []
    spazio_diviso = []
    old_cod = tot_int[-1][2]
    old_end = tot_int[-1][1] - 24 * 60
    for bi, ei, cod in tot_int:
        spazio = bi - old_end
        if cod == old_cod:
            if cod == "ac":
                spazio_ac.append(spazio)
            else:
                spazio_aj.append(spazio)
        else:
            spazio_diviso.append(spazio)
        old_end = ei
        old_cod = cod
    def new_spazi(tempo, spazio_list):
        tempo_ipotetico = tempo - sum(spazio_list)
        # print 'tempo_ipotetico {}'.format(tempo_ipotetico)
        # print sorted(spazio_list, key=lambda x: -x)
        for n_spazio, durata_spazio in enumerate(sorted(spazio_list, key=lambda x: -x)):
            # print "n spazio in {}".format(n_spazio)
            tempo_ipotetico += durata_spazio
            # print 'tempo_ipotetico {}'.format(tempo_ipotetico)
            if tempo_ipotetico >= 0:
                break
        # print "n spazio out {}".format(n_spazio)
        return (n_spazio + 1) * 2

    if tempo_ac - sum(spazio_ac) < 0:
        # sovraccarico ac
        return len(spazio_diviso) + new_spazi(tempo=tempo_ac, spazio_list=spazio_ac)

        pass
    elif tempo_aj - sum(spazio_aj) < 0:
        # sovraccarico aj
        return len(spazio_diviso) + new_spazi(tempo=tempo_aj, spazio_list=spazio_aj)
    else:
        # no sovraccarichi
        return len(spazio_diviso)


risultati = []
with open("B-large.in") as f:
    t = int(f.readline())
    print "t", t
    risultati = []
    for i in range(t):
        # print "\n"
        # n = int(f.readline())
        # print "n", n, i
        row = f.readline().strip()
        ac, aj = [int(c) for c in row.split(" ")]

        print ac, aj
        # print "ac"
        intervalli_ac = []
        for j in range(ac):
            row = f.readline().strip()
            ci, di = [int(c) for c in row.split(" ")]
            # print ci, di
            intervalli_ac.append((ci, di, "ac"))
        # print "aj"
        intervalli_aj = []
        for j in range(aj):
            row = f.readline().strip()
            ci, di = [int(c) for c in row.split(" ")]
            intervalli_aj.append((ci, di, "aj"))
        s = solve(int_ac=intervalli_ac, int_aj=intervalli_aj)
        print "solve: {}".format(s)
        risultati.append(s)
        # print "sol", sol
# assert sol == IMPOSSIBLE or len(sol) == int(row.split(" ")[0]), sol
#         risultati.append(solve(row))
# # print "risultati\n", risultati
with open("outBLarge.txt", "w") as out:
    for i, r in enumerate(risultati):
        out.write("Case #{}: {}\n".format(i+1, r))
