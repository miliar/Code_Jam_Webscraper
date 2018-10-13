def solve(N, Q, E, S, D, U, V):
    horses = []
    last_min = 0
    for i in range(N - 1):
        horses.append([E[i], S[i], last_min])
        current_min = 10e15
        for j, horse in enumerate(horses):
            horse[0] -= D[i][i + 1]
            if horse[0] < 0:
                horse[2] = 10e15
            else:
                horse[2] += D[i][i + 1] / S[j]
                if current_min > horse[2]:
                    current_min = horse[2]
        last_min = current_min
    return min(map(lambda x: x[2], horses))

def main():
    T = input()
    for i in xrange(1, T + 1):
        N, Q = map(int, raw_input().strip().split())
        E = []
        S = []
        D = []
        U = []
        V = []
        for j in range(N):
            e, s = map(int, raw_input().strip().split())
            E.append(e)
            S.append(float(s))
        for j in range(N):
            dis = map(int, raw_input().strip().split())
            D.append(dis)
        for j in range(Q):
            u, v = map(int, raw_input().strip().split())
            U.append(u)
            V.append(v)
        print 'Case #{0}: {1}'.format(i, solve(N, Q, E, S, D, U, V))

if __name__ == '__main__':
    main()
