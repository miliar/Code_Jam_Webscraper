from math import pi


def solve():
    n, k = map(int, input().split())
    pancakes = [list(map(int, input().split())) for i in range(n)]
    sides = [(r * h, r) for r, h in pancakes]
    sides.sort(reverse=True)
    res = []
    for i, side in enumerate(sides):
        a, r = side
        area = [a]
        if k > 1:
            for j in range(len(sides)):
                if j != i and sides[j][1] <= r:
                    area.append(sides[j][0])
                    if len(area) == k:
                        break
        res.append(r * r + 2 * sum(area))
    return pi * max(res)


def main():
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
