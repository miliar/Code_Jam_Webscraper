c, C = 0, int(input())
while c != C:
    c += 1

    T = tuple(map(int, input().split()))
    (N, S, p), T = T[:3], T[3:]

    a = 0
    for t in T:
        if t >= p:
            if t >= 3*p-2:
                a += 1
            elif S != 0 and t >= 3*p-4:
                S -= 1
                a += 1
    
    print("Case #%d:" % c, a)
            
