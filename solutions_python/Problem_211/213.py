T = int(input())

case = 0

while case < T:
    case += 1
    N, K = [int(x) for x in input().split()]
    U = float(input())

    pis = sorted([float(x) for x in input().split()])

    for changed in range(N):
        x = (U + sum(pis[0:changed + 1])) / (changed + 1)
        # print('x = ', x, ' changed = ', changed, ' sum = ', sum(pis[0:changed + 1]))
        if x > 1:
            continue

        if changed < N - 1:
            if x < pis[changed + 1]:
                break

    pis[0:changed + 1] = [x] * (changed + 1)

    # print(pis)

    prod = 1.0
    for ii in range(N):
        prod *= pis[ii]

    print("Case #{}: {:.10f}".format(case, prod))
