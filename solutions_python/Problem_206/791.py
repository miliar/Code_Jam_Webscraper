

NUM_TESTS=int(raw_input())

def solve(horses, D, N):
    t = 0
    for h in horses:
        t = max(t, (D - h[0]) / h[1])

    return D / t

for case_num in range(1, NUM_TESTS+1):

    (D, N) = map(int, raw_input().split(' '))
    horses = [None] * N
    for i in range(N):
        horses[i] = map(float, raw_input().split(' '))
    speed = solve(horses, D, N)
    print 'Case #{0}: {1}'.format(case_num, speed)

