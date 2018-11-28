def solve(r, t):
    r += 1
    i = 0
    s = 0
    while s <= t:
        s += r**2 - (r-1)**2
        r += 2
        i += 1
    return i-1

if __name__ == '__main__':
    for n in range(int(input())):
        print('Case #{}: {}'.format(n+1, solve(*(map(int, input().split(' '))))))
