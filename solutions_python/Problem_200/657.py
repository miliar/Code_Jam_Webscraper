T = int(input())

for t in range(T):

    N = [int(x) for x in input()]

    last = 0
    for i in range(len(N)):
        if N[i] < last:
            break
        last = N[i]
    else:
        print("Case #{}: {}".format(t+1, "".join(map(str, N))))
        continue

    first = i

    N[first-1] = N[first-1] - 1
    for i in range(first, len(N)):
        N[i] = 9

    i = first - 2
    while i >= 0 and N[i] > N[i+1]:
        N[i] = N[i+1]
        N[i+1] = 9
        i -= 1
    if i == -1 and N[0] == 0:
        N.pop(0)
        for i in range(first-1):
            N[i] = 9

    i = 0
    while N[i] == 0:
        i += 1
    print("Case #{}: {}".format(t+1, "".join(map(str, N[i:]))))
