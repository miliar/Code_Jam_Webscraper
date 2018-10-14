#! /usr/bin/env python3
# 2017 - Qualification
import fileinput


def find_stalls(n, k):
    stalls = [False] * (n + 2)
    stalls[0] = True
    stalls[-1] = True
    for _ in range(k):
        min_val, max_val, i = find_stall(stalls)
        stalls[i] = True
        # print(''.join('O' if x else '.' for x in stalls))  # DEBUG
    return max_val, min_val


def find_stall(stalls):
    l = [0] * len(stalls)
    curr = 0
    for i in range(len(l)):
        l[i] = curr
        curr = 0 if stalls[i] else curr + 1

    r = [0] * len(stalls)
    curr = 0
    for i in range(len(r) - 1, -1, -1):
        r[i] = curr
        curr = 0 if stalls[i] else curr + 1

    s = list(zip(l, r))
    mins = [-1 * min(a, b) for a, b in s]
    maxes = [-1 * max(a, b) for a, b in s]

    stats = sorted((s_min, s_max, s_i) for s_min, s_max, s_i
                   in zip(mins, maxes, range(len(stalls)))
                   if not stalls[s_i])
    min_val, max_val, i = stats[0]
    return -1 * min_val, -1 * max_val, i


def main(reader=fileinput.input()):
    t = int(reader.readline())
    for i in range(t):
        n, k = map(int, reader.readline().split())
        max_val, min_val = find_stalls(n, k)
        print('Case #{}: {} {}'.format(i + 1, max_val, min_val))


if __name__ == '__main__':
    main()
