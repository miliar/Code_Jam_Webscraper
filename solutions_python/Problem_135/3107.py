t=int(input())
for c in range(t):
    a1=int(input())
    r1 = []
    for i in range(4):
        if i == a1-1:
            r1 = list(map(int,input().split(' ')))
            continue
        input()
    a2=int(input())
    r2 = []
    for i in range(4):
        if i == a2-1:
            r2 = list(map(int,input().split()))
            continue
        input()
    intersections = 0
    number = -1
    for i in range(4):
        for j in range(4):
            if r1[i] == r2[j]:
                intersections += 1
                number = r1[i]

    if intersections == 0:
        print('Case #{0}: {1}'.format(c+1,'Volunteer cheated!'))
    elif intersections == 1:
        print('Case #{0}: {1}'.format(c+1,number))
    else:
        print('Case #{0}: {1}'.format(c+1,'Bad magician!'))

