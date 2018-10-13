import pdb

t = int(input())

for i in range(t):
    s = input().split(" ")
    n = int(s[0])

    u = float(input())

    p = [float(x) for x in input().split(" ")]

    p.sort()

    current = p[0]
    p.pop(0)
    count=1

    while u > 0:
        while p and p[0] <= current:
            p.pop(0)
            count += 1
        if p:
            top = p[0]
        else:
            top = 1
        
        if (not p) or (top - current) * count > u:
            current += u/count
            current = min(current, 1)
            u=0
        else:
            u -= (top-current) * count
            current = top

    result = current ** count
    for q in p:
        result *= q

    print("Case #{}: {}".format(i+1, result))
