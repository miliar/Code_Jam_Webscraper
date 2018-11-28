T = int(input())

for t in range(1, T+1):
    N = int(input())

    l = list(str(N))
    l = list(map(int, l))

    for i in range(len(l)-1, 0, -1):
        if l[i-1] > l[i]:
            l[i-1] -= 1
            for j in range(i, len(l)):
                l[j] = 9

    l = list(map(str, l))
    ans = int("".join(l))

    print("Case #" + str(t) + ": " + str(ans))

