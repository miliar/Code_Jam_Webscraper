for t in range(int(input())):
    N = '0' + input() + '9'
    N = [int(n) for n in reversed(N)]
    for i in range(len(N)-1):
        if N[i] < N[i+1]:
            for j in range(1, i+1):
                N[j] = 9
            N[i+1] -= 1

    res = ''.join(reversed([str(n) for n in N[1:-1]])).lstrip('0')
    print(f'Case #{t+1}: {res}')
