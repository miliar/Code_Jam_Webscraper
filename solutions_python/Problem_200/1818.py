from sys import stdin

T = int(stdin.readline())
for case in range(1, T + 1):
    N = int(stdin.readline())
    digits = []
    while N != 0:
        digits = [N % 10] + digits
        N /= 10

    for i in range(len(digits) - 1, 0, -1):
        if digits[i - 1] > digits[i]:
            digits[i - 1] -= 1
            j = i
            while j < len(digits) and digits[j] != 9:
                digits[j] = 9
                j += 1

    tidy = 0
    base = 1
    for i in range(0, len(digits)):
        tidy += digits[-1 - i] * base
        base *= 10

    print("Case #%d: %d" % (case, tidy))

