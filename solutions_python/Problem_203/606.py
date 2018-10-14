# cake.py
def test(m, r, c):
    for x in range(r):
        if m[x] != "?" * c:
            for y in range(c):
                start = c
                if m[x][y] == "?": start = y
                for y2 in range(1, c - start):
                    if m[x][start + y2] != "?":
                        m[x] = m[x][:start] + m[x][start + y2] * y2 + m[x][start + y2:]
                        break
            for y in range(1, c + 1):
                if m[x][-y] != "?":
                    m[x] = m[x][:-y] + m[x][-y] * y
                    break
    for x in range(r):
        start = r
        if m[x] == "?" * c: start = x
        for x2 in range(1, r - start):
            if m[start + x2] != "?" * c:
                m = m[:start] + [m[start + x2] for i in range(x2)] + m[start + x2:]
                break
    for x in range(1, r + 1):
        if m[-x] != "?" * c:
            m = m[:-x] + [m[-x] for i in range(x)]
            break
    return m

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    r, c = [int(s) for s in input().split(" ")]
    m = [input() for x in range(r)]
    print("Case #{}:".format(i))
    ans = test(m, r, c)
    for x in range(r):
        print(ans[x])
