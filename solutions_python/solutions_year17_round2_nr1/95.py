def solve(D, data):
    Ks, Ss = zip(*data)
    dists = [D - K for K in Ks]
    times = [d / S for d, S in zip(dists, Ss)]
    time = max(times)
    return D / time

def read_case():
    D, N = map(int, input().split(' '))
    data = [map(int, input().split(' ')) for _ in range(N)]

    return (D, data)

T = int(input())

solutions = [solve(*read_case()) for _ in range(T)]

for i, x in enumerate(solutions):
    print("Case #{}: {}". format(i+1, x))
