def func(s, k):
    total = 0
    for c in range(0, len(s)):
        if s[c] == '-':
            if (len(s) - c) < k:
                total = 'IMPOSSIBLE'
                break

            total = total + 1
            for j in range(c, c+k):
                if s[j] == '+':
                    s = s[:j] + '-' + s[j+1:]
                else:
                    s = s[:j] + '+' + s[j+1:]
    return total

t = int(input())

for i in range(1, t + 1):
    s, k = input().split(" ")
    print("Case #{}: {}".format(i, func(s, int(k))))
