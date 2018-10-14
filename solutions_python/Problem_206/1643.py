from heapq import heappush, heappop, heapify


def meeting_time(x1, v1, x2, v2):
    assert(x2 >= x1)
    if x1 == x2:
        return 0

    if v1 == v2:
        return 10**15

    return (x2 - x1) / (v1 - v2)


def solve(test_num):
    D, N = map(int, input().split())

    horses = sorted([tuple(map(int, input().split())) for i in range(N)]) + [(D, 0)]

    Q = [(meeting_time(x, v, *horses[idx+1]), idx, idx+1)
         for idx, (x, v) in enumerate(horses[:-1])]

    heapify(Q)
    
    res_t = 0
    merged = [False for i in range(len(horses))]
    next_horse = [i+1 for i in range(len(horses))]
    prev_horse = [i-1 for i in range(len(horses))]
    while len(Q) > 0:
        t, idx, neigh_idx = heappop(Q)
        if t < 0 or merged[idx] or next_horse[idx] != neigh_idx:
            continue

        res_t = t
        merged[idx] = True
        prev = prev_horse[idx]
        next_horse[prev] = neigh_idx
        if prev != -1:
            heappush(Q, (meeting_time(*horses[prev], *horses[neigh_idx]),
                         prev, neigh_idx))

    print("Case #{}: {}".format(test_num, D/res_t))


T = int(input())

for t in range(T):
    solve(t+1)
