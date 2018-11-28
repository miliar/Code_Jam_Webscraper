"""
Problem C

@author: Krisztian Balog
"""


def solve(n, k):
    """Straightforward simulation. I have no time for this shit."""
    o = [True] + [False] * n + [True]  # whether it's occupied
    # initialize Ls and Rs
    Ls = [-1] + [i for i in range(n)] + [-1]
    Rs = Ls[::-1]  # Ls reversed

    for i in range(k):
        # find where min(Ls,Rs) is maximal
        min_ = 0
        for j in range(n+1):
            if not o[j]:
                if min(Ls[j], Rs[j]) > min_:
                    min_ = min(Ls[j], Rs[j])

        # check if there is more than one
        pos = None
        max_ = 0
        for j in range(n+1):
            if not o[j]:
                if min(Ls[j], Rs[j]) == min_:
                    if (pos is None) or (pos is not None and max(Ls[j], Rs[j]) > max_):
                        pos = j
                        max_ = max(Ls[j], Rs[j])

        # take pos
        maxs = max(Rs[pos], Ls[pos])
        mins = min(Rs[pos], Ls[pos])

        o[pos] = True
        Rs[pos] = -1
        Ls[pos] = -1

        # update Ls and Rs
        l = pos  # index of first occupied left to position taken
        while l > 0 and not o[l - 1]:
            l -= 1
        for x in range(pos - l):
            Ls[l + x] = x
            Rs[l + x] = pos - l - x - 1

        r = pos  # index of first occupied right to position taken
        while r <= n and not o[r + 1]:
            r += 1
        for x in range(r - pos):
            Ls[pos + x + 1] = x
            Rs[pos + x + 1] = r - pos - x - 1

    return str(maxs) + " " + str(mins)


def run(infile, outfile):
    with open(infile, "r") as f:
        t = int(f.readline().strip())
        cases = [f.readline().strip() for i in range(t)]
    with open(outfile, "w") as f:
        for i, c in enumerate(cases):
            tmp = c.split()
            sol = solve(int(tmp[0]), int(tmp[1]))
            print(sol)
            f.write("Case #" + str(i + 1) + ": " + str(sol) + "\n")


if __name__ == "__main__":
    run("C-small-1-attempt0.in", "C-small-1-attempt0.out")
