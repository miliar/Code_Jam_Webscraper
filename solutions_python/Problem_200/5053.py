import sys
inp = sys.stdin.read().strip().split("\n")[1:]

def solve(i):
    def isinc(i):
        i = list(map(int, list(str(i))))
        return all(j<=k for j,k in zip(i, i[1:]))

    i = int(i)
    for j in range(i,0,-1):
        if isinc(j):
            return j

for e, i in enumerate(inp):
    print("Case #{0}: {1}" . format(e+1, solve(i)))