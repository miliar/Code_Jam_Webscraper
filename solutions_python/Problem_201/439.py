def value(s, idx):
    if idx == 0:
        if s%2 == 0:
            return s//2, s//2 - 1
        return (s//2, s//2)
    if not idx%2:
        return value(s//2 - (not s%2), idx//2 - 1)
    return value(s//2, idx//2)

def solve(d):
    v = value(d[0], d[1] - 1)
    return str(v[0]) + ' ' + str(v[1])

f = open('in.txt')

cases = int(f.readline())
for i in range(1, cases + 1):
    t = f.readline()
    d = [int(v) for v in t.split()]
    print('Case #%s: '%i + solve(d))
