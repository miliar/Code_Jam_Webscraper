
t = int(raw_input())

all_data = [raw_input().split() for i in range(t)]
all_data = [[int(i[0]), int(i[1])] for i in all_data]


def cal(N, K):
    stalls = {N: 1}
    for i in range(K):
        max_range = max(stalls)
        pos_l = (max_range - 1) / 2
        pos_r = (max_range - 1) - pos_l

        stalls[max_range] -= 1
        if stalls[max_range] <= 0:
            del stalls[max_range]
        stalls[pos_r] = stalls.get(pos_r, 0) + 1
        stalls[pos_l] = stalls.get(pos_l, 0) + 1
    return pos_l, pos_r


for i in range(t):
    r = cal(*all_data[i])
    print 'Case #{0}: {1} {2}'.format(i+1, max(r), min(r))
