T = int(raw_input())
for i in range(T):
    C, F, X = map(float, raw_input().split())
    sum = 0
    n = 0
    while True:
        time1 = C/(2+n*F)+X/(2+(n+1)*F)
        time2 = X/(2+n*F)
        if time1<time2:
            sum += C/(2+n*F)
            n += 1
        else:
            sum += time2
            break
    print "Case #"+str(i+1)+": "+"%.7f"%sum
    
