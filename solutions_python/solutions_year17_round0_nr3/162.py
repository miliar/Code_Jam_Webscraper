T = int(input())

def opt(c1, c2):
    max1, min1 = c1
    max2, min2 = c2
    if min1 < min2:
        return c1
    elif min1 > min2:
        return c2
    else:
        if max1 > max2:
            return c2
        else:
            return c1

results = {}

# assuming K <= N
def solve_problem(N, K):
    if not((N,K) in results):
        if (K == 1):
            results[(N,K)] = (N//2, (N-1)//2)
        else:
            # perfect split
            N_g = (N-1)//2
            N_d = N//2
            if (K-1)//2 == 0:
                results[(N,K)] = solve_problem(N_d, K//2)
            else:
                results[(N,K)] = opt(solve_problem(N_g, (K-1)//2), solve_problem(N_d, K//2))

    return results[(N,K)]

for i in range(T):
    N, K = [int(x) for x in input().split(' ')]
    mx, mn = solve_problem(N,K)
    print("Case #%d: %d %d" % (i+1,mx,mn))
