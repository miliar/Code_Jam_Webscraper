from sys import stdin, stderr

L = stdin.readlines()
n = int(L[0])
N = 2000000
R = {}
for i in range(1, N + 1):
    l = len(str(i))
    s = str(i) * 2
    q = min(map(int, [s[j:j + l] for j in range(l) if s[j] != '0']))
    if (not q in R):
        R[q] = []
    R[q].append(i)
    if i % 10000 == 0:
        print(q, i, file=stderr)
R = list(R[x] for x in R)
#print(R)
iter = 1

for l in L[1:]:
    a, b = map(int, l.split())
    ans =  0
    for x in R:
        t = len(list(u for u in x if a <= u <= b))
        ans += t * (t - 1) // 2
    print("Case #%d: %d" % (iter, ans))
    print("Case #%d: %d" % (iter, ans), file=stderr)

    iter += 1
