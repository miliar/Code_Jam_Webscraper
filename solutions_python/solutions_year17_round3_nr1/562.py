import math

def get_answer(N, K, pan):

    sorted_h = sorted(pan, key=lambda x: x[2]*x[1], reverse=True)

    selected = sorted_h[:K]
    sorted_out = sorted(sorted_h[K:], key=lambda x: x[1], reverse=True)
    sorted_sel = sorted(sorted_h[:K], key=lambda x: x[1], reverse=True)


    area = sorted_sel[0][1] * sorted_sel[0][1] * math.pi
    for sel in selected:
        area += 2 * sel[1] * sel[2] * math.pi

    idx = 0
    while idx < len(sorted_out) and sorted_out[idx][1] > sorted_sel[0][1]:
        max_r = sorted_out[idx]
        min_h = selected[-1]

        if max_r[1] > sorted_sel[0][1]:
            diff_r = max_r[1]*max_r[1]*math.pi - sorted_sel[0][1]*sorted_sel[0][1]*math.pi
            diff_h = 2*min_h[1]*min_h[2]*math.pi - 2*max_r[1]*max_r[2]*math.pi

            if diff_h < diff_r:
                area = area - diff_h + diff_r
                break
        idx += 1

    return area


t = int(input())
for i in range(1, t + 1):
    N, K = input().split(' ')
    N, K = int(N), int(K)

    pan = []
    for j in range(N):
        r, h = input().split(' ')
        r, h = int(r), int(h)
        pan.append((j, r, h))

    answer = get_answer(N, K, pan)
    print("Case #{}: {}".format(i, answer))
