

testcases = int(input())

for t in range(testcases):
    a, b = input().split()

    result = 0
    current = 0
    for s in b:
        s = int(s)
        current = current + s - 1
        if current < 0:
            result += abs(current)
            current = 0

    print("Case #%d: %d" % (t + 1, result))
