#!/usr/bin/env python
import sys

def solve_one(d, horses):
    vs = []
    for k, s in horses:
        v = float(d) * s / (d - float(k))
        vs.append(v)
    return str(min(vs))

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
        d,n = map(int, next_line().split())
        horses = []
        for i in range(n):
            k, s = map(int, next_line().split())
            horses.append((k, s))
        ans = solve_one(d, horses)
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

    
