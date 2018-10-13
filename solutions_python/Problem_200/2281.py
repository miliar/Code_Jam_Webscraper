def solve(n):
    for _ in range(len(n) + 1):
        n = solve_once(n)
    return n

def solve_once(n):
    p = n[0]
    for i, d in enumerate(n[1:]):
        if d < p:
            if p > '1':
                return n[:i] + str(int(p) - 1) + '9'* (len(n) - i - 1)
            else:
                return '9'*(len(n) - 1)
        p = d
    return n

def tidy(n):
    n = str(n)
    p = n[0]
    for c in n[1:]:
        if c < p:
            return False
        p = c
    return True


def solve_brute(n):
    n = int(n)
    while True:
        if tidy(n):
            return n
        n = n - 1

for i in range(int(input())):
    print('Case #{}: {}'.format(i+1, solve(input())))
