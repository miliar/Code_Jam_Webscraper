import sys

def distance_from(start, end, D):
    distance = 0
    for i in range(start, end):
        distance += D[i][i+1]
    return distance

def get_best_route(N, E, S, D, route):
    U, V = route
    assert U == 1
    assert V == N

    best_routes = [-1] * N
    best_routes[N-1] = 0
    for city in range(N-2, -1, -1):
        for next_hop in range(city+1, N):
            # using the horse at city
            d = distance_from(city, next_hop, D)
            if d != -1 and d <= E[city]:
                time_taken = d * 1.0 / S[city] + best_routes[next_hop]
                if best_routes[city] == -1 or best_routes[city] > time_taken:
                    best_routes[city] = time_taken

    return best_routes[0]


def solve():
    N, Q = map(int, sys.stdin.readline().rstrip().split())

    E = []
    S = []
    for i in range(N):
        e, s = map(int, sys.stdin.readline().rstrip().split())
        E.append(e)
        S.append(s)

    D = []
    for i in range(N):
        row = map(int, sys.stdin.readline().rstrip().split())
        D.append(row)

    routes = []
    for i in range(Q):
        U, V = map(int, sys.stdin.readline().rstrip().split())
        routes.append((U, V))

    best_routes = []
    for route in routes:
        best_route =  get_best_route(N, E, S, D, route)
        best_routes.append(best_route)

    return ' '.join(map(lambda x: '{:.8f}'.format(x), best_routes))


def main():
    T = int(sys.stdin.readline().rstrip())
    for t in range(1, T+1):
        answer = solve()
        print 'Case #{}: {}'.format(t, answer)

if __name__ == "__main__":
    main()
