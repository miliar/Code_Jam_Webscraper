def f(s):
    s = list(map(int, s))
    # print(s)
    j = 0
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            j = i
            break
    else:
        return ''.join(list(map(str,s)))
    for i in range(j):
        if s[i] == s[j]:
            j = i
            break
    # print(j)
    s[j] -= 1
    for i in range(j+1, len(s)):
        s[i] = 9
    s = list(map(str,s))
    s = int(''.join(s))
    return s

T = int(input())
for case in range(1, T+1):
    a = input()
    ans = f(a)
    print("Case #%s: %s" % (case, ans))

