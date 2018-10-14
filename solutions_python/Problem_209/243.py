from math import pi

T = int(input())

case = 0


while case < T:
    case += 1
    N, K = [int(x) for x in input().split()]
    dims = []
    for ii in range(N):
        dims.append([int(x) for x in input().split()])

    best_area = -1

    for ii in range(N):
        bottom = dims[ii]

        rest = [(r, h) for idx, (r, h) in enumerate(dims)
                if r <= bottom[0] and idx != ii]

        if len(rest) < K - 1:
            continue

        rest.sort(key=lambda x: -x[0] * x[1])
        chosen = rest[:K - 1]

        area = pi * bottom[0] ** 2 + 2 * pi * bottom[0] * bottom[1] + \
            sum(2 * pi * r * h for r, h in chosen)

        # print('ii = {}; bottom = {}; chosen = {}; area = {}'
        #       .format(ii, bottom, chosen, area))

        best_area = max(best_area, area)

    print("Case #{}: {:.10f}".format(case, best_area))
