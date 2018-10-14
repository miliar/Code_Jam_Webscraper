def solve(a, k):
    ans = 0
    for i in range(len(a)-k+1):
        if a[i] == -1:
            ans += 1
            for j in range(i, i + k):
                a[j] *= -1
    for e in a:
        if e == -1:
            return 'IMPOSSIBLE'
    return str(ans)

def conv(s):
    a = []
    for c in s:
        if c == '-':
            a.append(-1)
        else:
            a.append(1)
    return a

lines = [l.split() for l in open('A-large.in')]
T = int(lines[0][0])
for i in range(T):
    print('Case #%d: %s' % (i+1, solve(conv(lines[i+1][0]), int(lines[i+1][1]))))
