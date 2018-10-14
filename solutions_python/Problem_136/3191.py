T = int(raw_input())
C = [0.0 for i in range(T)]
F = [0.0 for i in range(T)]
X = [0.0 for i in range(T)]
for i in range(T):
    C[i], F[i], X[i] = map(float,raw_input().split())

#print C, F, X

f = open('cookie_ans.txt', 'w')

#time takes rate (r), cost (c), inc (f), cookies needed (x), and current # cookies (p)
def time(r, c, f, x, p):
    t = x/r+p
    while ((x/(r+f)) + p + c/r) < t:
        p += c/r
        r += f
        t = x/r + p
    return t

ans = [0.0 for i in range(T)]
for i in range(T):
    ans[i] = time(2.0, C[i], F[i], X[i], 0.0)
    f.write("Case #%d: %.7f\n" %(i+1,ans[i]))
