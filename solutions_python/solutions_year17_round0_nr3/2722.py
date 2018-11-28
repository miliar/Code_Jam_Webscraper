import sys

def draw_gaps(gaps):
    print("Gaps: %s" % gaps)
    print('#', end='')
    for gap in gaps:
        print('.' * gap, end='')
        print('#', end='')
    print()

def find_biggest_gap(gaps):
    max_gap, max_gap_index = -1, []
    for i, gap in enumerate(gaps):
        if gap > max_gap:
            max_gap = gap
            max_gap_index = i

    return max_gap_index


def bathroom_stalls(N, K):
    gaps = [N]
    for i in range(K):
        max_gap_index = find_biggest_gap(gaps)
        max_gap = gaps[max_gap_index]
        Ls = (max_gap - 1) // 2
        Rs = (max_gap - 1) // 2 + (max_gap - 1) % 2
        gaps = gaps[0:max_gap_index] + [Ls] + [Rs]  + gaps[max_gap_index + 1:]
        #draw_gaps(gaps)

    return max(Ls, Rs), min(Ls, Rs)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        T = int(f.readline())
        for i in range(T):
            N, K = map(int, f.readline().split())
            a, b = bathroom_stalls(N, K)
            print("Case #%d: %d %d" % (i + 1, a, b))
