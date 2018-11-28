t = int(input())
for i in range(t):
    n = input()
    start, untidy_idx = 0, -1
    for j in range(1, len(n)):
        if n[j - 1] > n[j]:
            untidy_idx = start
            break
        elif n[j - 1] < n[j]:
            start = j

    if untidy_idx == -1:
        print('Case #%d: %s' % (i + 1, n))
    else:
        result = ''
        for j in range(untidy_idx):
            result += n[j]
        result += str(int(n[untidy_idx]) - 1)
        for j in range(untidy_idx + 1, len(n)):
            result += '9'

        if result[0] == '0':
            print('Case #%d: %s' % (i + 1, result[1:]))
        else:
            print('Case #%d: %s' % (i + 1, result))
