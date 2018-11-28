def flip(st):
    global ans
    ans += 1
    st = ''.join([str(int(not (int(one)))) for one in st])
    return st


t = int(input())
for i in range(1, t + 1):
    s, k = input().split()
    k = int(k)
    a = ''
    ans = 0
    for j in range(len(s)):
        if s[j] == '-':
            a += '0'
        else:
            a += '1'
    if a[-1] == '0':
        a = a[:-k] + flip(a[-k:])
    for j in range(len(s)-2, -1, -1):
        if a[j] == '0':
            if j-k+1 >= 0:
                a = a[:j-k+1] + flip(a[j-k+1:j+1]) + a[j+1:]
            else:
                ans = -1
                break
    if ans != -1:
        print("Case #{}: {}".format(i, ans))
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))