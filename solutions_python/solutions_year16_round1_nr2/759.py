"""
Problem B

@author: Krisztian Balog
"""

def solve(rows):
    num = {}
    for row in rows:
        val = [int(v) for v in row.split()]
        for v in val:
            num[v] = num.get(v, 0) + 1
    missing = []
    for k,v in num.items():
        if v % 2 == 1:
            missing.append(k)
    missing.sort()
    return " ".join([str(s) for s in missing])


def run(infile, outfile):
    with open(infile, "r") as f:
        with open(outfile, "w") as fout:
            t = int(f.readline().strip())
            for i in range(t):
                n = int(f.readline().strip())
                rows = [f.readline().strip() for i in range(2*n-1)]
                sol = solve(rows)
                print(sol)
                fout.write("Case #" + str(i + 1) + ": " + sol + "\n")

if __name__ == "__main__":
    run("B-large.in", "B-large.out")