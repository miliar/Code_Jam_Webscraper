import sys

T = int(sys.stdin.readline())
tests = []
for i in range(T):
    D, N = sys.stdin.readline().split(" ")
    D = float(D)
    N = int(N)
    horses = []
    for n in range(N):
        K, S = sys.stdin.readline().split(" ")
        K = float(K)
        S = float(S)
        horses.append((K, S))
    tests.append((D, horses))


def compute_min_time_arrival(dist, horses):
    tmp_time = 0
    for i, (k, s) in enumerate(horses):
        t = (dist-k)/s
        if t > tmp_time:
            tmp_time = t
    return tmp_time


for nb, t in enumerate(tests):
    dist, horses = t
    tm = compute_min_time_arrival(dist, horses)
    res = dist/tm
    sys.stdout.write("Case #{}: {}\n".format(nb+1, res))
