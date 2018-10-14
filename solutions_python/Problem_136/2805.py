f = open('cookiefilelarge.txt', 'r')
array = []
for line in f:
        array.append(map(float, line.split()))
number = int(float(''.join(map(str,array[0]))))
for n in range(1, number + 1):
    time = []
    C = array[n][0]
    F = array[n][1]
    X = array[n][2]
    rate = 2
    donewithoutbuying = X / rate
    letsbuyanother = (C / rate) + (X / (rate + F))
    while donewithoutbuying > letsbuyanother:
        buyanother = C / rate
        time.append(buyanother)
        rate = rate + F
        donewithoutbuying = X / rate
        letsbuyanother = (C / rate) + (X / (rate + F))
    else:
        if X < C:
            print ("Case #" + str(n) + ": " + str(X / rate))
        else:
            time.append(donewithoutbuying)
            timeuntilend = sum(time)
            totaltime = round(timeuntilend, 7)
            print ("Case #" + str(n) + ": " + str(totaltime))
