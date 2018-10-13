def solve(n):
    ans = list()
    digits = list(map(int, list('{}'.format(n))))
    digits.reverse()
    ans += [digits[0]]
    for i_digit in range(1, len(digits)):
        if ans[-1] >= digits[i_digit]:
            ans += [digits[i_digit]]
        else:
            ans = [9] * len(ans)
            ans += [digits[i_digit] - 1]
    while ans[-1] == 0:
        del ans[-1]
    ans.reverse()
    return ''.join(map(str, ans))


T = int(input())
for t in range(1, T + 1):
    N = int(input())

    ANS = solve(N)
    print("Case #{}: {}".format(t, ANS))
