
def solve(d, hs):
    t = max((d-v[0])/v[1] for v in hs)
    return str(d/t)

f = open('a.in')

cases = int(f.readline())
for i in range(1, cases + 1):
    d, h = (int(v) for v in f.readline().split())
    hs = []
    for j in range(h):
        s = f.readline().split()
        hs.append((int(s[0]), int(s[1])))
    print('Case #%s: '%i + solve(d, hs))
