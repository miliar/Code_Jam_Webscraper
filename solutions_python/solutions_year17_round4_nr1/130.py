data = r"""3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1"""


def solve_one(p, gs):
    counts = [0 for i in range(p)]
    for g in gs:
        counts[g % p] += 1
    if p == 2:
        return counts[0] + (counts[1] // 2) + (counts[1] % 2)
    elif p == 3:
        ngroups = counts[0] + min(counts[1], counts[2])
        residual = max(counts[1], counts[2]) - min(counts[1], counts[2])
        ngroups += (residual // 3)
        if residual % 3 != 0:
            ngroups += 1
        return ngroups
    else:
        assert p == 4
        ngroups = counts[0]
        ngroups += min(counts[1], counts[3])
        res1 = max(counts[1], counts[3]) - min(counts[1], counts[3])
        ngroups += counts[2] // 2
        res2 = counts[2] % 2
        ngroups += (res1 // 4)
        res1 = res1 % 4
        if res1 + 2 * res2 > 4:
            ngroups += 2
        elif res1 + 2 * res2 > 0:
            ngroups += 1
        return ngroups


def solve(data):
    lines = iter(data.split("\n"))
    T = int(next(lines))
    res = []
    for ncase in range(1, T + 1):
        n, p = map(int, next(lines).split())
        gs = list(map(int, next(lines).split()))
        res.append("Case #%d: %d" % (ncase, solve_one(p, gs)))
    return "\n".join(res)


def solve_files(infile, outfile):
    with open(infile, "rt") as input, open(outfile, "wt") as output:
        solution = solve(input.read())
        output.write(solution)