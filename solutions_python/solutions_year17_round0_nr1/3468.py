def solve(s, k):
    n = len(s)
    a = ['-'] * len(s)
    for i in range(n):
        if s[i] == '-':
            a[i] = '-'
        else:
            a[i] = '+'

    count = 0
    for i in range(n-k+1):
        if a[i] == '+':
            continue
        count += 1
        for j in range(k):
            if a[i+j] == '-':
                a[i+j] = '+'
            else:
                a[i+j] = '-'

    for i in range(n):
        if a[i] == '-':
            return "IMPOSSIBLE"
        
    return str(count)

t = int(input())
for i in range(1, t + 1):
    s, k = input().split(" ")
    k = int(k)

    ret = solve(s, k)
    print ("Case #%d: %s" % (i, ret))

