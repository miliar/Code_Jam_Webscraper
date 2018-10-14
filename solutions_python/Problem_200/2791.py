
t = int(input())
for _ in range(t):
    n = input()
    if min(n) == '0' and n[0] == '1':
        print('Case #', _ + 1, ': ', '9' * (len(n) - 1), sep = '')
        continue
    flag = True
    for i in range(len(n) - 1):
        if (n[i] > n[i + 1]):
            flag = False
            break
    if flag:
        print('Case #', _ + 1, ': ', n, sep = '')
        continue
    res = 0
    for i in range(1, len(n)):
        if (n[i - 1] <= n[i] and ord(n[i - 1]) + 1 <= ord(n[i])):
            res = i
        else:
            break
    x = n[:res + 1]
    x = x[:-1] + chr(ord(x[-1]) - 1)
    x += '9' * (len(n) - res - 1)
    print('Case #', _ + 1, ': ', x, sep = '')