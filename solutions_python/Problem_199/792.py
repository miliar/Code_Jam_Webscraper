def isHappy(t):
    happy = True
    for x in t:
        if x != '+':
            happy = False

    return happy

t = int(input())
for i in range(1, t + 1):
    [_s, _k] = input().split(" ")

    s = list(_s)
    k = int(_k)
    count = 0
    for m in range(len(s)-k+1):
        if s[m] == '-':
            count += 1
            for n in range(k):
                if s[m + n] == '-':
                    s[m + n] = '+'
                else:
                    s[m + n] = '-'

    if isHappy(s):
        print("Case #{}: {}".format(i, count))
    else:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))

