with open("A-large.in", "r") as f:
    testCases = int(f.readline())
    for t in range(testCases):
        data = f.readline().split()
        maxS = int(data[0])
        s = list(map(int, list(data[1])))

        total = s[0]
        added = 0
        for i in range(1, len(s)):
            if total < i:
                added += i - total
                total += i - total
            total += s[i]
        print("Case #%d: %d" % (t + 1, added))
