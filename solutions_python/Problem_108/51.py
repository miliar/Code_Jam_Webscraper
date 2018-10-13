def solve(problem):
    D, vines = problem
    d0, l0 = vines.pop(0)
    assert(d0 <= l0)
    best = [(d0, d0)]
    for d, l in vines:
        best = [(d_, dl_) for (d_, dl_) in best if d_ + dl_ >= d]
        if not best:
            return "NO"
        dl = max(min(l, d - d_) for (d_, dl_) in best)
        best.append((d, dl))

    if any(d + dl >= D for (d, dl) in best):
        return "YES"
    return "NO"

def problems(fin):
    N = int(fin.next())
    for l in xrange(N):
        n = int(fin.next())
        vines = []
        for i in xrange(n):
            line = fin.next()
            vines.append(map(int, line.split(" ")))
        D = int(fin.next())
        yield D, vines

def main():
    with open("problem_1_large.in") as fin:
        with open("problem_1_large.out", "w") as fout:
            for n, problem in enumerate(problems(fin)):
                ans = solve(problem)
                ans = "Case #{0}: {1}\n".format(n + 1, ans)
                print ans,
                fout.write(ans)

if __name__ == "__main__":
    main()
