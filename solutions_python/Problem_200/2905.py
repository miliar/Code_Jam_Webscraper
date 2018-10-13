def remove_leading_zeros(l):
    for i in range(len(l)):
        if l[i] != 0:
            return l[i:]


def solve(N):
    i = len(N)
    for _ in range(len(N)):
        for i in range(len(N) - 1):
            if N[i] > N[i + 1]:
                N[i] -= 1
                for j in range(i + 1, len(N)):
                    N[j] = 9
                break

    return ''.join(map(str, remove_leading_zeros(N)))


T = int(input())
for t in range(T):
    N = [int(c) for c in input()]
    answer = solve(N)
    print('Case #{}: {}'.format(t + 1, answer))
