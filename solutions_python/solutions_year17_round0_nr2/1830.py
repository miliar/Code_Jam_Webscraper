#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :


def solve(N):
    for i in range(len(N)):
        N[i] = int(N[i])
    if len(N) > 1:
        for first_break in range(1, len(N)):
            if N[first_break - 1] > N[first_break]:
                break
        for i in range(first_break + 1, len(N)):
            N[i] = 9
    carry_over = False
    for i in range(len(N) - 1, -1, -1):
        if carry_over:
            if N[i] <= 0:
                N[i] = 9
            else:
                N[i] -= 1
                carry_over = False
        if i > 0 and N[i - 1] > N[i]:
            N[i] = 9
            carry_over = True
    return int(''.join(map(str, N)))


T = int(input())
for case_number in range(1, T + 1):
    N = list(input())
    print('Case #%d: %d' % (case_number, solve(N)))
