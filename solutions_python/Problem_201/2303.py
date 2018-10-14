import math




def cut(gap):
    if gap == 1:
        return (0, 0)
    return (math.ceil((gap - 1) / 2),
            max(math.floor((gap - 1) / 2), 0))


def largest_gap(gaps):
    return max(gaps.keys())


def cut_largest(gaps):
    gaps2 = gaps.copy()
    next_gap = largest_gap(gaps2)
    next_count = gaps[next_gap]
    (g1, g2) = cut(next_gap)
    del gaps2[next_gap]
    if g1 > 0:
        gaps2[g1] = gaps2.get(g1, 0) + next_count
    if g2 > 0:
        gaps2[g2] = gaps2.get(g2, 0) + next_count
    return gaps2


def consume(stalls, people):
    gaps = {stalls: 1}
    maxmin = cut(stalls)
    while people > 0:
        largest = largest_gap(gaps)
        largest_count = gaps[largest]
        people -= largest_count
        maxmin = cut(largest)
        gaps = cut_largest(gaps)
    return maxmin
        


T = int(input())

for i in range(1, T + 1):
    line = input().split()
    N = int(line[0])
    K = int(line[1])
    answer = consume(N, K)
    print('Case #{}: {} {}'.format(i, answer[0], answer[1]))
