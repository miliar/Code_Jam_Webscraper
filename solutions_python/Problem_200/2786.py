t = int(input())
for s in range(1, t + 1):
    N = [int(s) for s in list(input())]

    index = 0
    for i in range(len(N)):
        if len(N) == 1 or i == len(N) - 1:
            break
        if N[i + 1] < N[i]:
            N[i] -= 1
            N = N[:i + 1] + [9] * (len(N) - i - 1)
            break

    N = list(reversed(N))

    for i in range(len(N)):
        if len(N) == 1 or i == len(N) - 1:
            break
        if N[i + 1] > N[i]:
            N[i] = 9
            N[i + 1] -= 1

    N = list(reversed(N))
    N = [str(intt) for intt in N]
    N = int(''.join(N))

    print("Case #{}: {}".format(s, N))
