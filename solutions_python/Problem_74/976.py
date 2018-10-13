from sys import *

for t in range(input()):
    l = raw_input().split()
    current_orange = 1
    current_blue = 1
    last_orange = 0
    last_blue = 0
    total_time = 0
    for i in range(int(l[0])):
        color = l[2*i+1]
        button = int(l[2*i+2])
        if color == 'O':
            Dt = abs(current_orange-button) - last_blue
            if Dt < 0:
                Dt = 0
            Dt += 1
            total_time += Dt
            last_orange += Dt
            last_blue = 0
            current_orange = button
        elif color == 'B':
            Dt = abs(current_blue-button) - last_orange
            if Dt < 0:
                Dt = 0
            Dt += 1
            total_time += Dt
            last_orange = 0
            last_blue += Dt
            current_blue = button
        else:
            print 'FATAL ERROR'
            sys.exit()

    res = 'Case #{0}: {1}'.format(t+1,total_time)
    print res
