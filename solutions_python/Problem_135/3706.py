r = int(input())
s = r
while r > 0:
    x = int(input())
    a = []
    b = []
    k1 = 4
    while k1 > 0:
        n = input().split()
        if 5 - k1 == x:
            a.extend(n)
        k1 -= 1
    y = int(input())
    k2 = 4
    while k2 > 0:
        n = input().split()
        if 5 - k2 == y:
            b.extend(n)
        k2 -= 1
    
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(int(i))
    if len(c) > 1:
        print("Case #{}: Bad magician!".format(s + 1 - r))
    elif len(c) == 1:
        print("Case #{}:".format(s + 1 - r),c.pop())
    else:
        print("Case #{}: Volunteer cheated!".format(s + 1 - r))
    r -= 1
