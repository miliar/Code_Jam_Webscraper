def is_valid(combo):
    mx = max(combo)
    mn = min(combo)
    avg = float(round((mx + mn) / 2))
    if mn >= avg * 0.9 and mx <= avg * 1.1:
        return True
    return False


def smallest_index(combo):
    return combo.index(min(combo))


def solve(test_case):
    for i in xrange(len(test_case)):
        test_case[i].sort()
    found = 0
    while len(test_case[0]) > 0:
        A = [0] * len(test_case)
        for i in xrange(len(test_case)):
            if len(test_case[i]) == 0:
                break
            A[i] = test_case[i].pop(0)
        while not is_valid(A):
            idx = smallest_index(A)
            if len(test_case[idx]) == 0:
                break
            A[idx] = test_case[idx].pop(0)
        found += 1 if is_valid(A) else 0
    return found


t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    N, P = [int(s) for s in raw_input().split(" ")]
    R = [int(s) for s in raw_input().split(" ")]
    Q = []
    for k in range(0, N):
        Q.append([float(s) / R[k] for s in raw_input().split(" ")])
    sol = solve(Q)
    print("Case #{}: {}".format(i, sol))
