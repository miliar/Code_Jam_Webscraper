T = int(input())
for test_case in range(1, T+1):
    C, F, X = map(float, input().split())
    prev = X/2
    total_time = 0
    no_of_farms = 0
    farm_time = 0
    cookie_time = X/2
    while True:
        no_of_farms += 1
        farm_time += C/(2+F*(no_of_farms-1))
        cookie_time = X/(2+F*no_of_farms)
        total_time = farm_time + cookie_time
        if total_time > prev:
            break
        else:
            prev = total_time
    print("Case #{0}: {1:.7f}".format(test_case, prev))