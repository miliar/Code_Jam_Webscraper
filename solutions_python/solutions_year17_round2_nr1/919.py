from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    D,N = map(int, stdin.readline().strip().split())
    horses = [tuple(map(int, stdin.readline().strip().split())) for i in range(N)]

    horses.sort(key=lambda x: x[0], reverse=True)
    t = None

    for K,S in horses:
        u = (D-K)/S
        if t is None or u > t:
            t = u

    stdout.write("Case #{:d}: {:f}\n".format(case_num, D/t))
