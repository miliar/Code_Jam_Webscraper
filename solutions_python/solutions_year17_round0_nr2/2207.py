def get_last_tidy(n):
    num = [int(c) for c in str(n)]

    cursor = 0
    while cursor + 1 < len(num):
        if num[cursor] <= num[cursor + 1]:
            cursor += 1
            continue

        while (num[cursor - 1] > num[cursor] - 1) and (cursor > 0):
            cursor -= 1
        num[cursor] -= 1
        num[cursor + 1:] = [9] * (len(num) - cursor - 1)

        break

    return ''.join(map(str, num)).lstrip('0')

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    print('Case #%d: %s' % (case, get_last_tidy(n)))
