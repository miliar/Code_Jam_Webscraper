t = int(input())
for a0 in range(t):
    n, k = map(int, input().strip().split(' '))

    N = 1
    NN = 1
    while N <= n:
        NN += 1
        N = 2**NN - 1
    NN -= 1
    N = 2**NN-1
    a = n-N

    M = 1
    while M <= k:
        M *= 2
    M //= 2
    b = k - M

    result = ((N+1)//M - 2) + (a+M-1-b)//M

    if result % 2 == 0:
        print("Case #" + str(a0 + 1) + ": " + str(result//2) + " " + str(result//2))
    else:
        print("Case #" + str(a0 + 1) + ": " + str((result+1)//2) + " " + str((result-1)//2))

