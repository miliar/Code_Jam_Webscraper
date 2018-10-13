from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    N,K = map(int, stdin.readline().strip().split())
    U = float(stdin.readline().strip())
    P = list(map(float, stdin.readline().strip().split()))

    P.sort()
    lo = P[0]
    i = 0
    while not all(map(lambda x: x==1.0, P)) and U > 0.0:
        while i < len(P) and P[i] == lo:
            i += 1
        if i < len(P):
            target = P[i]
        else:
            target = 1.0
        if U < (target-lo)*i:
            target = lo + U/i
            U = 0
        else:
            U -= (target-lo)*i
        for j in range(i):
            P[j] = target
        lo = target

    total = 1
    for p in P:
        total *= p

    stdout.write("Case #{:d}: {:f}\n".format(case_num, total))
