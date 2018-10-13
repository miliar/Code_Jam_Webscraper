#Read Input - Absolutely 0 input checks

import fileinput

infile = fileinput.input()

p = infile.readline()

T = long(p)

t = 0

while t < T:
    t += 1
    O_curr, B_curr, O_dest, B_dest, last_move, time_lapse, total_time = 1, 1, 1, 1, 'X', 0, 0
    params = infile.readline()
    L = params.split()
    N = long(L.pop(0))
    while (len(L) > 0):
        turn = L.pop(0)
        if (turn == 'O'):
            O_dest = int(L.pop(0))
            if (last_move == 'B'):
                if (time_lapse < abs(O_curr - O_dest)):
                    time_lapse = abs(O_curr - O_dest) - time_lapse + 1
                    total_time += time_lapse
                else:
                    total_time += 1
                    time_lapse = 1
            else:
                time_lapse += abs(O_curr - O_dest) + 1
                total_time += abs(O_curr - O_dest) + 1
            O_curr = O_dest
            last_move = 'O'
            #print "O : ", total_time
        else:
            B_dest = int(L.pop(0))
            if (last_move == 'O'):
                if (time_lapse < abs(B_curr - B_dest)):
                    time_lapse = abs(B_curr - B_dest) - time_lapse + 1
                    total_time += time_lapse
                else:
                    total_time += 1
                    time_lapse = 1
            else:
                time_lapse += abs(B_curr - B_dest) + 1
                total_time += abs(B_curr - B_dest) + 1
            B_curr = B_dest
            last_move = 'B'
            #print "B : ", total_time
    print 'Case #%d: %d' % (t, total_time)