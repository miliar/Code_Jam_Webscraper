#!/usr/bin/env python
import sys

def solve_one_short(r, y, b):
    n = r + y + b
    l = [(r, 'R'), (y, 'Y'), (b, 'B')]
    l = list(sorted(l))
    q = [t[0] for t in l]
    s = [t[1] for t in l]
    if n == 1:
        return s[2]
    if q[0] + q[1] < q[2]:
        return "IMPOSSIBLE"
    if q[0] == 0:
        res = (s[1] + s[2]) * (n // 2)
        return res
    res = []
    for i in range(q[0]):
        res.append(s[0])
        res.append(s[2])
        q[2] -= 1
        if q[1] > q[2]:
            res.append(s[1])
            q[1] -= 1
    for i in range(q[2]):
        if res[-1] == s[2]:
            res.append(s[1])
            res.append(s[2])
        else:
            res.append(s[2])
            res.append(s[1])
    return "".join(res)

def solve_one(n, r, o, y, g, b, v):
    assert(n == r + o + y + g + b + v)
    # duals o - b, g - r, v - y
    IMPOSSIBLE = "IMPOSSIBLE"
    if o + b == n:
        if o != b:
            return IMPOSSIBLE
        else:
            return "OB" * (n // 2)
    if  g + r == n:
        if g != r:
            return IMPOSSIBLE
        else:
            return "GB" * (n // 2)
    if v + y == n:
        if v != y:
            return IMPOSSIBLE
        else:
            return "VY" * (n // 2)
    if (b <= o and o > 0) or (r <= g and g >0 ) or (y <= v and v > 0):
        return IMPOSSIBLE
    r -= g
    y -= v
    b -= o
    ans = solve_one_short(r, y, b)
    if ans == "IMPOSSIBLE":
        return "IMPOSSIBLE"
    ans = ans.replace("R", "R" + "GR" * g, 1)
    ans = ans.replace("Y", "Y" + "VY" * v, 1)
    ans = ans.replace("B", "B" + "OB" * o, 1)
    return ans
    
def test_one(n, r, o, y, g, b, v):
    from collections import defaultdict
    sets = [set("ROV"), set("YGO"), set("BVG")]
    ans = solve_one(n, r, o, y, g, b, v)
    if ans == "IMPOSSIBLE":
        return True
    if n != len(ans):
        return False
    d =  defaultdict(lambda: 0)
    for c in ans:
        d[c] += 1
    if r != d['R'] or o != d['O'] or y != d['Y'] or g != d['G'] or b != d['B'] or v != d['V']:
        return False
    for i in range(n):
        c1 = ans[(i + 1) % n]
        c2 = ans[i]
        for cols in sets:
            if (c1 in cols) and (c2 in cols):
                return False
    return True


def solve(data):
    def lines():
        for line in data.split("\n"):
            yield line
    lines_iter = lines()
    def next_line():
        return lines_iter.__next__()
    res = []
    T = int(next_line())
    cur_line = 1
    for ncase in range(1, 1 + T):
        # read test case
        n, r, o, y, g, b, v = map(int, next_line().split())
        ans = solve_one(n, r, o, y, g, b, v)
        if not (test_one(n, r, o, y, g, b, v)):
            print(n, r, o, y, g, b, v)
        res.append("Case #%d: %s" % (ncase, ans))
    return "\n".join(res)

def solve_files(infile, outfile):
    data = infile.read()
    result = solve(data)
    outfile.write(result)

def main():
    infile = sys.stdin
    outfile = sys.stdout
    if len(sys.argv) > 1:
        infile = open(sys.argv[1], "rt")
    if len(sys.argv) > 2:
        outfile = open(sys.argv[2], "wt")
    solve_files(infile, outfile)
    outfile.close()

if __name__ == "__main__":
    main()

    
