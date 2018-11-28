import sys

def solve():
    N, K = map(int, sys.stdin.readline().rstrip().split())
    U = float(sys.stdin.readline().rstrip())

    P = map(float, sys.stdin.readline().rstrip().split())
    P = sorted(P)

    best_prod = 1
    for i in range(N):
        best_prod *= P[i]

    level = 0
    for i in range(N):
        cost_to_level = 0
        for j in range(i):
            cost_to_level += P[i] - P[j]


        if cost_to_level > U:
            break


        #print cost_to_level, P[i]+ (U-cost_to_level)/(i+1),  (U-cost_to_level)/(i+1)
        if (U-cost_to_level) > (1-P[i])*(i+1):
            if abs((U-cost_to_level) - (1-P[i])*(i+1)) > 0.0000001:
                continue

        balance = (U-cost_to_level)/(i+1)
        level = P[i]+balance

        prod = (P[i]+balance)**(i+1)
        for j in range(i+1, N):
            prod *= P[j]

        #print prod, best_prod, i, level
        if prod >= best_prod:
            best_prod = prod

    test_prod = 1
    gainz = 0
    for i in range(N):
        if P[i] <= level:
            gainz += level - P[i]
            test_prod *= level
        else:
            test_prod *= P[i]

    #print gainz, U, best_prod, level, P
    assert abs(gainz-U) < 0.000001
    assert abs(test_prod-best_prod) < 0.000001

    return best_prod


def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        print 'Case #{}: {:.8f}'.format(t, solve())

if __name__ == "__main__":
    main()
