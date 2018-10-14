maxT = int(input())
t = 0
while t < maxT:
    t += 1
    s = list(input())
    s = s[::-1]
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            for j in range(i + 1):
                s[j] = '9'
            s[i + 1] = chr(ord(s[i + 1]) - 1)
    s = s[::-1]
    s = ''.join(s)
    print("Case #{}: {}".format(t, int(s)))
