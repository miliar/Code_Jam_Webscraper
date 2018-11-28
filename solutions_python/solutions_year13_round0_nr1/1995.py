import sys

sys.stdin = open('A-large-0.in', 'r')
sys.stdout = open('A-large-0.out', 'w')

T = int(input())

LINES = [
            [
                [0, 0],
                [0, 1],
                [0, 2],
                [0, 3],
            ],
            [
                [1, 0],
                [1, 1],
                [1, 2],
                [1, 3],
            ],
            [
                [2, 0],
                [2, 1],
                [2, 2],
                [2, 3],
            ],
            [
                [3, 0],
                [3, 1],
                [3, 2],
                [3, 3],
            ],
            [
                [0, 0],
                [1, 0],
                [2, 0],
                [3, 0],
            ],
            [
                [0, 1],
                [1, 1],
                [2, 1],
                [3, 1],
            ],
            [
                [0, 2],
                [1, 2],
                [2, 2],
                [3, 2],
            ],
            [
                [0, 3],
                [1, 3],
                [2, 3],
                [3, 3],
            ],
            [
                [0, 0],
                [1, 1],
                [2, 2],
                [3, 3],
            ],
            [
                [0, 3],
                [1, 2],
                [2, 1],
                [3, 0],
            ],
        ]


def solution():
    a = [list(input().strip()) for i in range(4)]
    try:
        input()
    except:
        pass
    for line in LINES:
        if sum((1 if a[foo[0]][foo[1]] in "XT" else 0) for foo in line) == 4:
            return "X won"
    for line in LINES:
        if sum((1 if a[foo[0]][foo[1]] in "OT" else 0) for foo in line) == 4:
            return "O won"
    if '.' not in ''.join((''.join(bar for bar in foo)) for foo in a):
        return 'Draw'
    else:
        return "Game has not completed"


for test in range(T):
    test += 1
    print("Case #%03d:" % test, end = ' ', file = sys.stderr)
    print("Case #%d: %s" % (test, solution()))
    print("OK", file = sys.stderr)
