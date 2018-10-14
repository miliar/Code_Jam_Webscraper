
def tidy_numbers(N):
    N = list(str(N))
    for i in range(len(N) - 1, 0, -1):
        current = int(N[i])
        next = int(N[i - 1])
        if current < next:
            N[i:] = '9' * len(N[i:])
            next = (next - 1) % 10
            N[i - 1] = str(next)
    return int(''.join(N))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = tidy_numbers(N)
    print('Case #{t}: {result}'.format(t=t, result=result))
