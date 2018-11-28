
tests = []

with open('input.in', 'r') as f:
    T = int(f.readline())
    for i in range(T):
        D, N = tuple(f.readline().strip().split(' '))
        D, N = int(D), int(N)
        hlist = []
        for j in range(N):
            Ki, Si = tuple(f.readline().strip().split(' '))
            Ki, Si = int(Ki), int(Si)
            hlist.append((Ki, Si))
        tests.append((D, N, hlist))

with open('output.out', 'w') as f:
    case = 1
    for D, N, hlist in tests:
        last_arrival = max([(D-k)/s for k,s in hlist])
        f.write("Case #%d: %f\n" % (case, D/last_arrival))
        case += 1

