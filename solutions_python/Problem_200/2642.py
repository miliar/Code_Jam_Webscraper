T = int(input())
for t in range(T):
    N = [int(i) for i in input()][::-1]
    for i in range(len(N) - 1):
        if N[i] < N[i + 1]:
            for j in range(i + 1):
                N[j] = 9
            N[i + 1] = N[i + 1 ] - 1
    N = [str(i) for i in N[::-1]]
    print('Case #%d: %d' % (t+ 1, int(''.join(N))))
