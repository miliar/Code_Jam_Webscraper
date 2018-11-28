from collections import defaultdict

def solve(r0, g0, r1, g1):
    d = defaultdict(list)
    for i in range(1, 16 + 1):
        d[(g0.index(i) // 4, g1.index(i) // 4)].append(i)

    r0 -= 1
    r1 -= 1
    if not d[(r0, r1)]:
        return "Volunteer cheated!"
    if len(d[(r0, r1)]) > 1:
        return "Bad magician!"
    return d[(r0, r1)][0]


def main():
    T = int(input())

    def read_grid():
        g = []
        for r in range(4):
            g.extend(map(int, input().split()))
        return g

    for tc in range(T):
        r0 = int(input())
        g0 = read_grid()
        r1 = int(input())
        g1 = read_grid()
        print("Case #{}: {}".format(tc + 1, solve(r0, g0, r1, g1)))


if __name__ == "__main__":
    main()
