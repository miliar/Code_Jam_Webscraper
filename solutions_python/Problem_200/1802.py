import sys


def solve(N):
    digits = [int(d) for d in str(N)]
    ans, i, maxd = [], 0, 1
    while i < len(digits) and digits[i] >= maxd:
        ans.append(digits[i])
        maxd = max(maxd, digits[i])
        i = i + 1
    if i == len(digits):
        return N
    i = i - 1
    ans[i] = ans[i] - 1
    if len(ans) > 1:
        while i >= 1 and ans[i] < ans[i - 1]:
            ans[i - 1] = ans[i - 1] - 1
            ans[i] = 9
            i = i - 1
    ans.extend([9] * (len(digits) - len(ans)))
    if ans[0] > 0:
        return int(''.join([str(d) for d in ans]))
    return int(''.join(['9'] * (len(digits) - 1)))


def main(fn):
    with open(fn, 'r') as fi:
        with open(fn + '.out', 'w') as fo:
            T = int(next(fi).strip())
            for t in range(1, T + 1):
                N = int(next(fi).strip())
                ans = solve(N)
                fo.write('Case #%d: %d\n' % (t, ans))


if __name__ == '__main__':
    main(sys.argv[1])
