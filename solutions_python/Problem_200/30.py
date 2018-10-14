def solve():
    N = [c for c in input()]
    L = len(N)
    for _ in range(L):
        for i in range(L - 1):
            if N[i] > N[i+1]:
                N[i] = chr(ord(N[i]) - 1)
                for j in range(i+1, L):
                    N[j] = '9'
    print(int(''.join(N)))


T = int(input())
for num in range(1, T+1):
    print('Case #' + str(num) + ': ', end='')
    solve()
