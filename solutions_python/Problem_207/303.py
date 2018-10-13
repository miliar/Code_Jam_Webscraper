

tc = int(input())
for inp in range(tc):
    FLAG = "IMPOSSIBLE"
    print("Case #%d: " % (inp + 1), end="")
    n, r, o, y, g, b, v = map(int, input().split())
    if o != 0 or g != 0 or v != 0:
        continue
    if r == 0:
        if y == b:
            print("YB" * (n // 2))
        else:
            print(FLAG)
        continue
    if y == 0:
        if r == b:
            print("RB" * (n // 2))
        else:
            print(FLAG)
        continue
    if b == 0:
        if r == y:
            print("RY" * (n // 2))
        else:
            print(FLAG)
        continue
    if r == y == b:
        print("RYB" * (n // 3))
        continue
    tc = min(r, y, b)
    r -= tc
    y -= tc
    b -= tc
    if r == y == 0:
        if b <= tc:
            print("BRBY" * b + "BRY" * (tc - b))
        else:
            print(FLAG)
        continue
    if r == b == 0:
        if y <= tc:
            print("YRYB" * y + "YRB" * (tc - y))
        else:
            print(FLAG)
        continue
    if y == b == 0:
        if r <= tc:
            print("RYRB" * r + "RYB" * (tc - r))
        else:
            print(FLAG)
        continue
    if r == 0:
        if y < b:
            if b - y <= tc:
                print("RBYB" * (b - y) + "RYB" * (tc - b + y) + "YB" * y)
            else:
                print(FLAG)
        else:
            if y - b <= tc:
                print("RYBY" * (y - b) + "RBY" * (tc - y + b) + "BY" * b)
            else:
                print(FLAG)
        continue
    if y == 0:
        if r < b:
            if b - r <= tc:
                print("YBRB" * (b - r) + "YRB" * (tc - b + r) + "RB" * r)
            else:
                print(FLAG)
        else:
            if r - b <= tc:
                print("YRBR" * (r - b) + "YBR" * (tc - r + b) + "BR" * b)
            else:
                print(FLAG)
        continue
    if b == 0:
        if y < r:
            if r - y <= tc:
                print("BRYR" * (r - y) + "BYR" * (tc - r + y) + "YR" * y)
            else:
                print(FLAG)
        else:
            if y - r <= tc:
                print("BYRY" * (y - r) + "BRY" * (tc - y + r) + "RY" * r)
            else:
                print(FLAG)
        continue
