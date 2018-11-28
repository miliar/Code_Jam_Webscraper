def solve(i, n):
    if i < 0:
        return n
    elif n[i] <= n[i+1]:  # correct
        return solve(i - 1, n)
    else:
        return solve(i - 1, n[:i] + str(int(n[i]) - 1) + '9' * (len(n) - i - 1))


t = int(input())
for case in range(1, t + 1):
    n = input()
    n = '0' + n
    print('Case #{}: {}'.format(case, int(solve(len(n) - 2, n))))
