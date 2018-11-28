# Code: 1 = 1, i= 2, j = 3, k = 4

def mult(m, s, start, end):
    r = 1
    for i in range(start, end + 1):
        if r > 0:
            r = m[r-1][s[i]-1]
        else:
            r = -m[-r-1][s[i]-1]
    return r

m = [[1, 2, 3, 4],
     [2, -1, 4, -3],
     [3, -4, -1, 2],
     [4, 3, -2, -1]]

d = {'1':1, 'i':2, 'j':3, 'k':4}

f = open('C-small-attempt0.in', 'r')
o = open('out.txt', 'w')
T = f.readline()
T = int(T)
for i in range(1, T+1):
    l = f.readline()
    l = l.split()

    L = int(l[0])
    X = int(l[1])

    l = f.readline()
    l = l[:-1]
    s = l * X
    s=map(d.get, s)
    leng = len(s)
    ans = "ERROR"

    j = 0
    r1 = 1
    while (j < leng - 2 and r1 != 2):
        r1 = mult(m, s, 0, j)
        j += 1
    if j >= leng - 2:
        ans = "NO"

    k = j
    r2 = 1
    while (k < leng - 1 and r2 != 3):
        r2 = mult(m, s, j, k)
        k += 1

    if k >= leng - 1:
        ans = "NO"

    r3 = mult(m, s, k, leng - 1)

    if r1 == 2 and r2 == 3 and r3 == 4:
        ans = "YES"
    else:
        ans = "NO"

    outline = "Case #%d: %s\n" % (i, ans)
    o.write(outline)

o.close()
