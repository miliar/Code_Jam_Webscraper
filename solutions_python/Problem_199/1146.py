
t = int(input())

for c in range(t):
    s, k = input().split()
    k = int(k)
    s = [True if ch == "+" else False for ch in s]

    counter = 0
    for i in range(len(s)-k+1):
        if not s[i]:
            s[i:i+k] = [not pan for pan in s[i:i+k]]
            counter += 1
    if all(s):
        print("Case #%d: %d" % (c+1, counter))
    else:
        print("Case #%d: IMPOSSIBLE" % (c+1))
