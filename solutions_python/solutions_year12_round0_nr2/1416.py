t = input()
for cases in range(t):
    
    a = map(int,raw_input().split())
    n, s, p = a[:3]
    a = a[3:]

    cnt = 0
    for x in a:
        if x == 0:
            if p == 0:
                cnt += 1
            continue
        p1 = 0
        if x % 3 == 0:
            p1 = x / 3
        else :
            p1 = x / 3 + 1

        if p1 >= p :
            cnt += 1
        else :
            if s == 0:
                continue
            p1 = 0
            if x % 3 == 2 :
                p1 = x / 3 + 2
            else :
                p1 = x / 3 + 1
            if p1 >= p:
                cnt += 1
                s -= 1

    print ("Case #" + str(cases + 1) + ": " + str(cnt))
