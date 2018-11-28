import sys


def run_case(inf):
    s_max, ps = inf.readline().split()
    s_max = int(s_max)
    s = [int(s) for s in ps]
    prev = friends = 0
    for i in range(s_max):
        req = i + 1
        total = prev + s[i] + friends
        if total < req:
            friends += req - total
        prev += s[i]

    return friends


def main():
    inf = sys.stdin
    outf = sys.stdout
    N = int(inf.readline())
    for i in range(N):
        result = run_case(inf)
        outf.write("Case #{}: {}\n".format(i + 1, result))

if __name__ == "__main__":
    main()