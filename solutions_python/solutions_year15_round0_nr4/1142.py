import math

f = open('out.txt', 'w')

cases = int( raw_input() )

for case in range(cases):
    
    XRC = [int(i) for i in str( raw_input() ).split()]

    squares = XRC[1] * XRC[2]

    answer = "RICHARD"
    gabe = 0
    
    if XRC[0] == 1:
        gabe = 1
    if XRC[0] == 2:
        if squares % 2 == 0:
            gabe = 1
    if XRC[0] == 3:
        if squares % 3 == 0:
            if XRC[1] > 1 and XRC[2] >= 3:
                gabe = 1
            if XRC[1] >= 3 and XRC[2] > 1:
                gabe = 1
    if XRC[0] == 4:
        if squares % 4 == 0:
            if XRC[1] > 2 and XRC[2] == 4:
                gabe = 1
            if XRC[1] == 4 and XRC[2] > 2:
                gabe = 1

    if gabe == 1:
        answer = "GABRIEL"
    
    print "Case #" + str(case + 1) + ": " + answer
    print >> f, "Case #" + str(case + 1) + ": " + answer

f.close()
