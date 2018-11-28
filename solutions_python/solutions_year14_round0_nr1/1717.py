import sys


def cases(filename):
    with open(filename, 'r') as f:
        t = int(f.readline().strip())
        for _ in range(t):
            ans1 = int(f.readline().strip())
            grid1 = [list(map(int, f.readline().strip().split())) for _ in range(4)]
            ans2 = int(f.readline().strip())
            grid2 = [list(map(int, f.readline().strip().split())) for _ in range(4)]
            yield (ans1, grid1, ans2, grid2)


def solve(ans1, grid1, ans2, grid2):
    cards1 = set(grid1[ans1 - 1])
    cards2 = set(grid2[ans2 - 1])
    chosen = cards1 & cards2
    if len(chosen) == 1:
        return chosen.pop()
    elif len(chosen) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: {} filename'.format(sys.argv[0]))
        sys.exit(1)
    for i, case in enumerate(cases(sys.argv[1]), 1):
        print('Case #{}: {}'.format(i, solve(*case)))
