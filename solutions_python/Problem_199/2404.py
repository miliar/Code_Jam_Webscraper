t = int(input())

for c in range(t):
    s, k = input().split()
    k = int(k)
    s = list(s)
    count = 0
    for e in range(len(s) - k + 1):
        if s[e] == '-':
            for f in range(k):
                s[e+f] = '-' if s[e+f] == '+' else '+'
            count += 1

    if set(s) != {'+'}:
        count = "IMPOSSIBLE"
    print("Case #{}: {}".format(c+1,count))
