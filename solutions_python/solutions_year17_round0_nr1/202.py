
fo = open("1.out", "w")
fi = open("1.in", "r")
n = int(fi.readline())
for i in range(0, n):
    cnt = 0
    s, k = fi.readline().split(' ')
    k = int(k)
    s = list(s)
    for j in range(0, len(s)):
        if s[j] == '-' and j + k - 1 < len(s):
            cnt += 1
            for l in range(0, k):
                s[l + j] = '+' if s[l + j] == '-' else '-'
        elif s[j] == '-' and j + k - 1 >= len(s):
            cnt = -1
            break
    if cnt == -1:
        fo.write('Case #{}: IMPOSSIBLE\n'.format(i+1))
    else:
        fo.write('Case #{}: {}\n'.format(i+1, cnt))
