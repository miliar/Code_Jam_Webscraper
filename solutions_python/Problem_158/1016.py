def f(x, a, b):
    gb = "GABRIEL"
    rch = "RICHARD"
    a, b = min(a, b), max(a, b)
    if x == 1:
        return gb
    elif x == 2:
        if a * b % 2 == 0:
            return gb
        else:
            return rch
    elif x == 3:
        if a == 1:
            return rch
        elif a == 2:
            if b == 3:
                return gb
            else:
                return rch
        elif a == 3:
            return gb
        elif a == 4:
            return rch
    elif x == 4:
        if a == 1:
            return rch
        elif a == 2:
            return rch
        elif a == 3:
            if b == 4:
                return gb
            else:
                return rch
        elif a == 4:
            return gb


fin = open("input.txt")
t = int(fin.readline())
for case in range(t):
    x, r, c = map(int, fin.readline().split())
    ans = f(x, r, c)
    print("Case #%i: %s" % (case + 1, ans))
fin.close()