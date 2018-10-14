f_in = open('D-small-attempt0.in', 'r')
f_out = open('D-small.out', 'w')

T = int(f_in.readline())

i = 1
for line in f_in:
    X, R, C = map(int, line.strip().split())

    if X == 1:
        winner = 'GABRIEL'
    elif X == 2:
        if R * C % 2 == 1:
            winner = 'RICHARD'
        else:
            winner = 'GABRIEL'
    elif X == 3:
        if R * C == 6 or R * C == 9 or R * C == 12:
            winner = 'GABRIEL'
        else:
            winner = 'RICHARD'
    elif X == 4:
        if R * C == 12 or R * C == 16:
            winner = 'GABRIEL'
        else:
            winner = 'RICHARD'

    f_out.write('Case #' + str(i) + ': ' + winner + '\n')

    i += 1

f_out.close()
f_in.close()
