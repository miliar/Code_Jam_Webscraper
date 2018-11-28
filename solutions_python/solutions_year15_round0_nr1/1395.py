n = int(input())
for I in range(1, n+1):
    result = 0
    standing = 0
    a, b = input().split()
    a = int(a)
    pos = 0
    for k in b:
        if (standing < pos):
            result += (pos - standing)
            standing = pos
        standing += int(k)
        pos += 1
    print("Case #%d: %d" % (I, result))
