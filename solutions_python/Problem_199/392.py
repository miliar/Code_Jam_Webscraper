N = int(input())
for c in range(1, N + 1):
    s, k = input().split()
    k = int(k)
    ls = list(s)
    i = 0
    ans = 0
    impossible = False
    while i < len(ls):
        if ls[i] == '+':
            i += 1
            continue
        if i == len(ls) - k and ls[i:] == ['-'] * (len(ls) - i):
            ans += 1
            break
        if i >= len(ls) - k and ls[i:] != ['+'] * (len(ls) - i):
            impossible = True
            break
        for j in range(i, i + k):
            if ls[j] == '+':
                ls[j] = '-'
            else:
                ls[j] = '+'
        ans += 1
    if impossible:
        print('Case #%d: IMPOSSIBLE' % c)
    else:
        print('Case #%d: %d' % (c, ans))
