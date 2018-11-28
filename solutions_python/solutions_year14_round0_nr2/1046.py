# Code Jam 2014 - Qualification Round
# Problem B: Cookie Clicker Alpha
# chamrtom

T = int(raw_input())

for t in range(1, T+1):
    [C, F, X] = map(float, raw_input().split())

    speed = 2.0
    cookies = 0.0
    time = 0.0

    while cookies < X:
        if (X-cookies)/speed <= (C-cookies)/speed:
            time += (X-cookies)/speed
            break
        else:
            if (C-cookies)/speed + X/(speed+F) <= (X-cookies)/speed:
                time += (C-cookies)/speed
                cookies = 0.0
                speed += F
            else:
                time += (X-cookies)/speed
                break
    
    print "Case #{0}: {1:.7f}".format(t, time)
