import sys



def solve(N, Q, horses, distances, deliveries):
    # Small only.

    Bests = [float('inf') for _ in xrange(N)]
    Bests[0] = 0

    for i in xrange(N-1):
        speed = horses[i][1]
        dist_remaining = horses[i][0]
        t = Bests[i]
        j = i
        while j + 1 < N and dist_remaining >= distances[j][j+1]:
            t += float(distances[j][j+1]) / speed
            if t < Bests[j+1]:
                Bests[j+1] = t
            dist_remaining -= distances[j][j+1]
            j += 1

    return Bests[N-1]


def main():
    T = int(sys.stdin.readline().strip())

    for x in xrange(T):
        N, Q = map(int, sys.stdin.readline().split())
        horses = []
        for i in xrange(N):
            Ei, Si = map(int, sys.stdin.readline().split())
            horses.append((Ei, Si))
        distances = []
        for i in xrange(N):
            Dijs = map(int, sys.stdin.readline().split())
            assert len(Dijs) == N
            distances.append(Dijs)
        deliveries = []
        for k in xrange(Q):
            Uk, Vk = map(int, sys.stdin.readline().split())
            deliveries.append((Uk, Vk))

        ans = solve(N, Q, horses, distances, deliveries)
        print 'Case #%s: %s' % (x+1, ans)

if __name__ == '__main__':
    main()
