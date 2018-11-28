import sys

def solve(n):
    s = list(n)
    for i in range(len(s)-1,0,-1):
        if is_tidy("".join(s[i-1:i+1])):
            continue
        s = list(str(int("".join(s[0:i]))-1)) + ['9']*(len(s)-i)
    return "".join(s)

def is_tidy(s):
    return str(s) == "".join(sorted(str(s)))

def main(infile, outfile):
    with open(infile, "rt") as f:
        T = int(f.readline())
        sol = []
        for t in range(1, T + 1):
            S = f.readline().strip()
            ans = solve(S)
            sol.append("Case #{0}: {1}\n".format(t, int(ans)))
        print(sol)
    with open(outfile, "wt") as f:
        f.writelines(sol)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

