import sys

def get_lr(segment):
    start = segment[0]
    end = segment[1]
    middle = (start + end) / 2
    return middle - start - 1, end - middle - 1

def solve2(N, K):
    levels = [1]
    for i in range(1, 64):
        levels.append(levels[i - 1] * 2)

    count = 0
    l = len(levels)
    for i in range(1, l):
        if K + 1 <= levels[i]:
            count = levels[i - 1]
            break

    N += 1
    unit = N / count
    difference = K + 1 - count
    number_of_unit_plus_1 = N - unit * count
    if difference <= number_of_unit_plus_1 and N % count != 0:
        unit += 1

    middle = unit / 2
    return unit - middle - 1, middle - 1
    
def solve(N, K):
    segments = [[0, N + 1]]
    max_min_lr = 0
    max_max_lr = 0
    for i in range(0, K):
        max_min_lr = -1
        max_max_lr = -1
        current_segment = None
        for segment in segments:
            l, r = get_lr(segment)
            current_min = min(l, r)
            current_max = max(l, r)
            if current_min > max_min_lr:
                max_min_lr = current_min
                max_max_lr = current_max
                current_segment = segment
            elif current_min == max_min_lr:
                if current_max > max_max_lr:
                    max_max_lr = current_max
                    current_segment = segment

        middle = (current_segment[0] + current_segment[1]) / 2
        segments.append([middle, current_segment[1]])
        current_segment[1] = middle
        segments = sorted(segments, key=lambda s: s[0])

    return max_max_lr, max_min_lr

T = int(sys.stdin.readline())
for i in range(0, T):
    segments = sys.stdin.readline().split(' ')
    N = int(segments[0])
    K = int(segments[1])
    #ll, rr = solve(N, K)
    L, R = solve2(N, K)
    #print('Case #%d: %d %d' % (i + 1, ll, rr))
    print('Case #%d: %d %d' % (i + 1, L, R))

