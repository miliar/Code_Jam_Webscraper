cases = int(input())

for i in range(cases):
    info = input().strip('\n').split(' ')
    for j in range(3):
        info[j] = float(info[j])
    C = info[0] #Cookies for Farm
    F = info[1] #Farm bonus
    X = info[2] #Wincon

    time = -1
    pretime = -1
    total = 0
    R = 2
    while(1):
        time = X/R + total
        if (time > pretime and pretime > 0):
            break
        pretime = time
        pretotal = total
        
        farmtime = C/R
        total += farmtime
        R += F
    print("Case #" + str(i + 1) + ": %.7f" %pretime)
