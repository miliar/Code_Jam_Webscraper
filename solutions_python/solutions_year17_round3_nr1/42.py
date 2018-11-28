import math
n = int(input())
for test_case in range(1, n+1):
    N, K = [int(x) for x in input().split()]
    pks = []
    for _ in range(N):
        pks.append(tuple(int(x) for x in input().split()))
    pks = sorted(pks, key = lambda x: -x[0] * x[1])
    #print(pks)
    max_solution = -1
    for i, pk_max in enumerate(pks):
        (r_max, _) = pk_max
        pks_2 = pks[:i] + pks[i+1:]
        pks_2 = [(r, h) for (r, h) in pks_2 if r <= r_max]
        if len(pks_2) < K-1:
            continue
        max_pks2 = pks_2[:K-1] + [pk_max]
        solution = math.pi * r_max*r_max + sum(
            2*math.pi * r * h for (r, h) in
            max_pks2)
        max_solution = max(solution, max_solution)
    assert (max_solution != -1)
    print("Case #{}: {}".format(test_case, max_solution))

