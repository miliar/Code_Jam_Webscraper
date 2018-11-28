T = int(raw_input().strip())
for t in range(T):
    N = [int(c) for c in '{:d}'.format(int(raw_input().strip()))]
    if len(N) == 1:
        answer = N
    else:
        i = 0
        while i < len(N) - 1:
            if N[i] > N[i + 1]:
                break
            i += 1
        if i == len(N) - 1:
            answer = N
        else:
            N[i] -= 1
            while i > 0:
                if N[i - 1] <= N[i]:
                    break
                else:
                    N[i - 1] -= 1
                i -= 1
            pos = i + 1
            while pos < len(N):
                N[pos] = 9
                pos += 1
            answer = N

    S = ''
    for num in answer:
        S += '{:d}'.format(num)
    answer = int(S)

    print('Case #{:d}: {:d}'.format(t + 1, answer))
