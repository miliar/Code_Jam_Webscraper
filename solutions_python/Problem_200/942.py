import sys

def solve(N):
    if N < 10:
        return N

    last_digit = N % 10
    second_last_digit = (N / 10) % 10
    append_9 = False
    if second_last_digit > last_digit:
        append_9 = True
        previous = solve((N / 10 * 10 - 1) / 10)
    else:
        previous = solve(N / 10)
    if append_9 or previous % 10 > last_digit:
        return previous * 10 + 9
    return previous * 10 + last_digit

T = int(sys.stdin.readline())
for i in range(0, T):
    N = int(sys.stdin.readline())
    print('Case #%d: %d' % (i + 1, solve(N)))

