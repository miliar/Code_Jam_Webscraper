def capture_pos(arr1):
    count = arr1.count(1)
    prev_index = -1
    l = len(arr1)
    pos_arr = [(0, 0)] * l
    if count:
        next_index = arr1.index(1)
    else:
        next_index = l
    for j in range(prev_index + 1, next_index):
        pos_arr[j] = (j - prev_index - 1, next_index - j - 1)
    prev_index = next_index + 1 - 1
    for i in range(count - 1):
        next_index = arr1.index(1, next_index + 1)
        for j in range(prev_index + 1, next_index):
            pos_arr[j] = (j - prev_index - 1, next_index - j - 1)
        prev_index = next_index + 1 - 1
    for j in range(prev_index + 1, l):
        pos_arr[j] = (j - prev_index - 1, l - j - 1)
    min_pos = list(map(min, pos_arr))
    mi_pos = max(min_pos)
    if min_pos.count(mi_pos) == 1:
        result = min_pos.index(mi_pos)
        return pos_arr[result], result
    for i in range(l):
        if mi_pos != min_pos[i] or arr1[i] == 1:
            pos_arr[i] = (-1, -1)
    max_pos = list(map(max, pos_arr))
    ma_pos = max(max_pos)
    result = max_pos.index(ma_pos)
    return pos_arr[result], result


def mid(inp):
    N, K = map(int, inp.split(' '))
    if N <= K or (N > 1000 and K > (N * 0.52)):
        return '0 0'

    arr = [0] * N
    for i in range(K):
        out = capture_pos(arr)
        arr[out[1]] = 1
    return '%d %d' % (max(out[0]), min(out[0]))


for i in range(int(input().strip())):
    print("Case #%d: %s" % (i + 1, mid(input().strip())))
