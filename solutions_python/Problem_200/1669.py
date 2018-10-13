def solve(N):
    if len(N) < 2:
        return N
    i = 0
    while N[i] <= N[i + 1]:
        i += 1
        if i >= len(N) - 1:
            return N
    j = i
    while j > 0 and N[j - 1] == N[i]:
        j -= 1
    return (N[:j] + str(int(N[j]) - 1) + ('9' * (len(N) - j - 1)))

if __name__ == '__main__':
    for i in range(int(input())):
        print('Case #{}: {}'.format(i + 1, int(solve(input()))))
