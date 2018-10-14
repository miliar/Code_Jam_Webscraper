def flip(cakes, i, l):
    for j in range(i, i + l):
        cakes[j] = '-' if cakes[j] == '+' else '+'

def solve(case_id):
    cakes, l = input().split(' ')
    l = int(l)
    cakes = list(cakes)
    n = 0
    for i in range(len(cakes) - l + 1):
        if cakes[i] == '-':
            flip(cakes, i, l)
            n += 1
        # print(''.join(cakes))
    if all([c == '+' for c in cakes]):
        print('Case #{}: {}'.format(case_id, n))
    else:
        print('Case #{}: IMPOSSIBLE'.format(case_id))

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        solve(i + 1)
