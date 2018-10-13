import sys

def input():
    row = int(sys.stdin.readline())-1
    grid = [[int(x) for x in sys.stdin.readline().strip().split(' ')] for _ in range(4)]
    return grid[row]

def solve():
    row1 = set(input())
    row2 = set(input())
    intersect = row1 & row2
    return list(intersect)


T = int(sys.stdin.readline())
for t in range(1, T+1):
    r = solve()
    if len(r) == 1:
        sys.stdout.write('Case #%i: %i\n' % (t,r[0]))
    elif len(r) == 0:
        sys.stdout.write('Case #%i: Volunteer cheated!\n' % t)
    else:
        sys.stdout.write('Case #%i: Bad magician!\n' % t)
