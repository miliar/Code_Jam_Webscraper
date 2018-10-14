IN = open('input.txt', 'r')

T = int(IN.readline())

for ttt in xrange(1, T + 1):

    line = IN.readline().strip().split()

    N = int(line[0])
    
    L = [(line[i], int(line[i + 1])) for i in xrange(1, len(line), 2)]
    O = []
    B = []

    for robot, x in L:
        if robot == 'O':
            O.append(x)
        else:
            B.append(x)

    O.append(101)
    B.append(101)

    o = b = 1
    io = ib = 0
    Sum = 0
    
    for robot, x in L:
        if robot == 'O':
            while o != x:
                if o < x:
                    o += 1
                else:
                    o -= 1
                Sum += 1
                if b < B[ib]:
                    b += 1
                elif b > B[ib]:
                    b -= 1
            Sum += 1
            if b < B[ib]:
                b += 1
            elif b > B[ib]:
                b -= 1
            io += 1
        else:
            while b != x:
                if b < x:
                    b += 1
                else:
                    b -= 1
                Sum += 1
                if o < O[io]:
                    o += 1
                elif o > O[io]:
                    o -= 1
            Sum += 1
            if o < O[io]:
                o += 1
            elif o > O[io]:
                o -= 1
            ib += 1

    print 'Case #{}: {}'.format(ttt, Sum)
