
fo = open("1.out", "w")
fi = open("1.in", "r")
n = int(fi.readline())
for i in range(0, n):
    s = fi.readline()
    s = list(s)
    s.pop()
    cnt = -1
    for j in range(0, len(s) - 1):
        if s[j] > s[j + 1]:
            cnt = j
            break
    if cnt != -1:
        for j in range(cnt, -1, -1):
            if s[j] > s[j + 1]:
                s[j] = chr(ord(s[j]) - 1)
                cnt = j
        # print('Case #{}: {}\n'.format(i + 1, ''.join(s)))
        if s[0] == '0':
            s[0] = ''
            for j in range(1, len(s)):
                s[j] = '9'
        else:
            for j in range(cnt + 1, len(s)):
                s[j] = '9'
    fo.write('Case #{}: {}\n'.format(i + 1, ''.join(s)))
