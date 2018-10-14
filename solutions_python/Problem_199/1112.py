maxT = int(input())
t = 0
while t < maxT:
    t += 1
    str, k = input().split()
    k = int(k)
    str = list(str)
    r = 0
    for i in range(len(str) - k + 1):
        if str[i] == '-':
            for j in range(k):
                str[j + i] = '-' if str[j + i] == '+' else '+'
            r += 1
    for i in str:
        if i == '-':
            r = -1
    print("Case #{}: {}".format(t, r if r >= 0 else "IMPOSSIBLE"))    
