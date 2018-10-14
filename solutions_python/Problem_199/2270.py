def inverse(s):
    s = s.replace('-', '*')
    s = s.replace('+', '-')
    s = s.replace('*', '+')
    return s


for i in range(int(input())):
    s, k = input().split(' ')
    k = int(k)
    count = 0
    minus_pos = s.find('-')

    while 0 <= minus_pos < len(s) - k + 1:
        s = s[:minus_pos] + inverse(s[minus_pos:minus_pos + k]) + s[minus_pos + k:]
        count += 1
        minus_pos = s.find('-')

    if minus_pos == -1:
        print("Case #{}: {}".format(i + 1, count))
    else:
        print("Case #{}: {}".format(i + 1, "IMPOSSIBLE"))
