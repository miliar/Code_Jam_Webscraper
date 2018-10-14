
t = int(input())
for ii in range(1, t + 1):
    s, k = input().split()
    k = int(k)
    s = list(s)
    count = 0
    for i in range(0, len(s)):
        if s[i] == '-' and ((i + k) < (len(s) + 1)):
            count += 1
            for j in range(i, i + k):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
    flag = 0
    for i in range(0, len(s)):
        if s[i] == '-':
            flag = 1
    if flag:
        nig = "IMPOSSIBLE"
    else:
        nig = count

    print("Case #{}: {}".format(ii, nig))
