import sys

i = file(sys.argv[1], 'r')
o = file(sys.argv[2], 'w')

T = int(i.readline())
for t in range(1, T + 1):
    C, F, X = i.readline().split()
    C = float(C)
    F = float(F)
    X = float(X)

    bps = 2.0
    cur_score = 0.0
    time = 0.0
    best_time = 99999999999999999999999.0
    while time < best_time:
        sec_farm = C / bps
        total_x = (X)/bps+time

        if total_x < best_time:
            best_time = total_x
        time += sec_farm
        bps += F
    o.write('Case #'+str(t)+': '+str(best_time)+'\n')
    print t