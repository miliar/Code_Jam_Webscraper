import sys

def find_max_fresh(P, groups):
    mods = [0] * P
    for g in groups:
        mods[g % P] += 1
    sol = mods[0]
    if P == 2:
        sol += (mods[1]+1) / 2
    elif P == 3:
        mins = min(mods[1], mods[2])
        rest = max(mods[1], mods[2]) - mins
        sol += mins
        sol += (rest+2) / 3
    elif P == 4:
        mins = min(mods[1], mods[3])
        rest = max(mods[1], mods[3]) - mins
        sol += mins
        mods[1] -= mins
        mods[3] -= mins
        sol += mods[2] / 2
        mods[2] = mods[2] % 2
        if mods[2] == 1:
            if rest < 2:
                return sol + 1
            else:
                rest -= 2
                sol += 1
        sol += (rest+3) / 4
    return sol

if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        N, P = [int(part) for part in sys.stdin.readline().split()]
        groups = [int(part) for part in sys.stdin.readline().split()]
        assert len(groups) == N
        sol = find_max_fresh(P, groups)
        print "Case #%d: %d" % (i+1, sol)
