#!python3

def intersections(wires):
    count = 0
    #print(wires)

    for i, (ai, bi) in enumerate(wires):
        for j, (aj, bj) in enumerate(wires[i + 1:]):
            count += int( (ai - aj) * (bi - bj) < 0 )

    return count


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    wires = [list(map(int, input().split())) for _ in range(N)]
    print('Case #{}: {}'.format(t, intersections(wires)))

