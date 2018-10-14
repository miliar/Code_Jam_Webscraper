import math

tests = []

with open('input.in', 'r') as f:
    T = int(f.readline())
    for t in range(T):
        N, Q = tuple(f.readline().strip().split(' '))
        N, Q = int(N), int(Q)
        horses = []
        for i in range(N):
            Ei, Si = tuple(f.readline().strip().split(' '))
            Ei, Si = int(Ei), int(Si)
            horses.append((Ei, Si))
        all_dists = []
        for i in range(N):
            Dists = f.readline().strip().split(' ')
            if i != N-1:
                d = int(Dists[i+1])
            else:
                d = 0
            all_dists.append(d)
        f.readline()
        tests.append((N, Q, horses, all_dists))


with open('output.out', 'w') as f:
    case = 1
    for N, Q, horses, all_dists in tests:

        opt = [0.0] * N

        for i in range(N - 2, -1, -1):
            best = float('inf')
            end = horses[i][0]
            total = 0
            for j in range(i+1, N):
                end -= all_dists[j - 1]
                total += all_dists[j - 1]
                if end < 0:
                    opt[i] = best
                    break
                if best >= opt[j] + total / horses[i][1]:
                    best = opt[j] + total / horses[i][1]
                opt[i] = best

        f.write("Case #%d: %s\n" % (case, opt[0]))

        case += 1






