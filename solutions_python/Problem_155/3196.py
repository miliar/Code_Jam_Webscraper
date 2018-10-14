tests = int(input())
results = []
for j in range(tests):
    m, s = input().split()
    m = int(m)
    s = [int(x) for x in s]

    people = 0
    for i in range(1, len(s)):
        x = sum(s[:i])
        if x < i and s[i] > 0:
            s[0] += i - x
            people += i - x
    results.append("Case #{0}: {1}".format(j + 1, people))
for r in results:
    print(r)
