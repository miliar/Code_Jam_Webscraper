def flip(s):
    return s.replace('+', '.').replace('-', '+').replace('.', '-')

def solve(p, n):
    if len(p) < n:
        return 'Impossible'
    c = 0

    while len(p) > n:
        if p[0] == '-':
            p = flip(p[:n])+ p[n:]
            c += 1
        p = p[1:]

    if p == '-' * n:
        return c + 1
    elif p == '+' * n:
        return c
    return 'Impossible'

for i in range(int(input())):
    p, n = input().split()
    print('Case #{}: {}'.format(i+1, solve(p, int(n))))
