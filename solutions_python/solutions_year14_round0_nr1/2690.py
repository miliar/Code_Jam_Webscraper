t = input()
for i in range(t):
    x = input()
    ar1 = []
    ar2 = []
    for j in range(4):
        ar1.append(map(int,raw_input().split()))
    y = input()
    for j in range(4):
        ar2.append(map(int,raw_input().split()))
    l = list(set(ar1[x-1]) & set(ar2[y-1]))
    print l
    if len(l) == 1:
        print "Case #1:", l[0]
    elif len(l) > 1:
        print "Case #2: Bad magician!"
    else:
        print "Case #3: Volunteer cheated!"
