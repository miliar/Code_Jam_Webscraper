import os
import os.path

def solve(matrix):
    wp = []
    owps = []

    num_teams = len(matrix)
    for l in matrix:
        wins = [0]*(num_teams+1)
        game = [0]*(num_teams+1)
        for i,g in enumerate(l):
            if g == '1':
                for j in range(num_teams+1):
                    if j == i: continue
                    wins[j] += 1
                    game[j] += 1
            elif g == '0':
                for j in range(num_teams+1):
                    if j == i: continue
                    game[j] += 1
        wp.append(float(wins[-1]) / float(game[-1]))
        op = []
        for j in range(num_teams):
            op.append(float(wins[j]) / float(game[j]))
        owps.append(op)

    owp = []
    for i,l in enumerate(matrix):
        o = 0.0
        count = 0
        for j,g in enumerate(l):
            if g != '.':
                o += owps[j][i]
                count += 1
        o = o / count
        owp.append(o)

    rpi = []
    for i,l in enumerate(matrix):
        r = 0.25 * wp[i]
        r += 0.5 * owp[i]
        oowp = 0.0
        count = 0
        for j,g in enumerate(l):
            if g != '.':
                oowp += owp[j]
                count += 1
        oowp = oowp / count
        r += 0.25 * oowp
        rpi.append(r)

    return rpi

def RPI(path):
    fin = open(path)
    out_path = os.path.splitext(path)[0] + ".sol"
    fout = open(out_path, "w")

    num_cases = int(fin.readline().strip())

    for i in range(num_cases):
        length = int(fin.readline().strip())
        matrix = []
        for l in range(length):
            matrix.append(fin.readline().strip())
        sol = solve(matrix)
        fout.write("Case #%i:\n" % (i+1))
        for s in sol:
            fout.write("%.10f\n" % s)

    fout.close()
    fin.close()
