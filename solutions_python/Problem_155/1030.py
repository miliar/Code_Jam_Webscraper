T = int(input())
for I in range(1, T+1):
    s = raw_input().split()
    l = int(s[0])
    s = s[1]
    tmp = 0
    result = 0
    for i in range(0, l+1):
        if (i > tmp):
            result = max(result, i - tmp)
        tmp += int(s[i])
    print("Case #%d: %d" % (I, result))
