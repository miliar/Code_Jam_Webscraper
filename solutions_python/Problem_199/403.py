from sys import stdin

def solve(t):
    line = stdin.readline().split(' ')
    s = list(line[0])
    k = int(line[1])
    n = len(s)
    cnt = 0
    for start in range(0, n - k + 1):
        if s[start] == '-':
            cnt += 1
            for i in range(start, start + k):
                s[i] = ('-' if s[i] == '+' else '+')
    check = True
    for i in range(n - k, n):
        if s[i] == '-':
            check = False
            break

    print('Case #' + str(t + 1) + ': ', end='')
    if check:
        print(str(cnt))
    else:
        print('IMPOSSIBLE')


T = int(stdin.readline())
for t in range(0, T):
    solve(t)
