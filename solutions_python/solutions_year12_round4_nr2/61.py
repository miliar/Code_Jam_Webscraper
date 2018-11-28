def solve(problem):
    w, h, rs = problem
    rs_ = sorted(enumerate(rs), reverse=True, key=lambda x: x[1])
    x, y, ans = 0, 0, []
    while rs_:
        curr, R, R0 = 0, None, None
        while curr < len(rs_):
            i, r = rs_[curr]
            if not R is None:
                x_ = x + R + r
                if x_ > w:
                    curr += 1
                    continue
                x = x_
            else:
                R0, y = r, y and y + r or 0
                
            R = r
            pos = (x, y)
            assert(pos <= (w, h))
            ans.append((i, pos))
            rs_.pop(curr)
        y += R0

    ans = [pos for i, pos in sorted(ans)]
    for i0, (x0, y0) in enumerate(ans):
        for i1, (x1, y1) in enumerate(ans):
            if i0 >= i1:
                continue
            d2 = (x0 - x1)**2 + (y0 - y1)**2
            assert(d2 >= (rs[i0] + rs[i1])**2)
    return " ".join("{0} {1}".format(x, y) for x, y in ans)

def problems(fin):
    N = int(fin.next())
    for l in xrange(N):
        n, w, h = map(int, fin.next().split(" "))
        rs = map(int, fin.next().split(" "))
        yield w, h, rs

def main():
    with open("problem_2_small.in") as fin:
        with open("problem_2_small.out", "w") as fout:
            for n, problem in enumerate(problems(fin)):
                ans = solve(problem)
                ans = "Case #{0}: {1}\n".format(n + 1, ans)
                print ans,
                fout.write(ans)

if __name__ == "__main__":
    main()
