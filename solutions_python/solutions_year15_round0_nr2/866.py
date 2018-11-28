import sys


class InfiniteHouseOfPancakes:

    def solve_case_rec(self, p, w, l, M=None):
        if w > l:
            return l
        if M is None:
            M = {}
        k = "".join(map(str, sorted(p)))
        if k in M:
            return M[k]
        m = max(enumerate(p), key=lambda v: v[1])
        options = [max(p) + w]
        if max(p) > 1:
            for moving in range(1, m[1]):
                options.append(self.solve_case_rec(p[:m[0]] + [m[1] - moving] + p[m[0] + 1:] + [moving], w + 1, l, M))
        M[k] = min(options)
        return M[k]

    def solve_case(self, f):
        d = int(f.readline())
        p = map(int, f.readline().split(" "))
        return self.solve_case_rec(p, 0, max(p))

    def create_report(self, ci, r):
        r = ", ".join(map(str, r)) if isinstance(r, (list, tuple)) else str(r)
        return "Case #" + str(ci) + ": " + r

    def solve(self, f):
        t = int(f.readline())
        results = []
        for c in range(t):
            results.append(self.solve_case(f))
        return "\n".join(map(lambda c: self.create_report(c[0] + 1, c[1]), enumerate(results)))

    def solve_and_save(self, out, f):
        out.write(self.solve(f))

if __name__ == "__main__":
    ihop = InfiniteHouseOfPancakes()

    if len(sys.argv) < 2:
        ihop.solve_and_save(sys.stdout, sys.stdin)
    else:
        f = open("./in/" + sys.argv[1] + ".in", 'r')
        o = open("./out/" + sys.argv[1] + ".out", 'w')
        ihop.solve_and_save(o, f)
        f.close()
        o.close()
