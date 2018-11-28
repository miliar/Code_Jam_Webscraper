import sys


def main():
    t = int(sys.stdin.readline())
    cases = []
    for i in range(t):
        cases.append(int(sys.stdin.readline()))
    print(solve(cases))

def solve(cases):
    def case(c):
        if tidy(c):
            return str(c)
        else:
            return case(c - 1)

    def tidy(c):
        c = str(c)
        for i in range(0, len(c) - 1):
            if c[i] > c[i + 1]:
                return False
        return True

    ans = []
    for i, c in enumerate(cases):
        ans.append("Case #{}: {}".format(i + 1, case(c)))
    return "\n".join(ans)

if __name__ == '__main__':
    main()
