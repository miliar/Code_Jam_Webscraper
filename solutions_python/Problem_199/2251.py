def foo(s, k, c):
    num = 0
    for i in range(len(s) - k):
        if s[i] != c:
            for j in range(i, i + k):
                s[j] = '+' if s[j] == '-' else '-'
            num += 1
    cc = s[-k]
    if cc != c:
        num += 1
    for i in range(-k, 0):
        if cc != s[i]:
            return -1
    return num


f = open("QA.in", "r")
out = open("QA.out", "w")
n = int(f.readline())
for t in range(n):
    line = f.readline().split()
    s1, s2, k = list(line[0]), list(line[0]), int(line[1])
    p = foo(s1, k, '+')
    if p == -1:
        out.write("Case #" + str(t + 1) + ": IMPOSSIBLE\n")
    else:
        out.write("Case #" + str(t + 1) + ": " + str(p) + "\n")
out.close()