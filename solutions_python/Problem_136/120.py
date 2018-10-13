import sys
f = sys.stdin
T = int(f.readline().strip())
for i in range(1,T+1):
    C, F, X = [float(x) for x in f.readline().strip().split(' ')]
    best_time = X/2.0
    N = 0.0
    time_to_buy = 0.0
    while True:
        time_to_buy += C / (2.0 + N*F)
        time_to_fin = X / (2.0 + (N+1)*F)
        if (time_to_fin + time_to_buy <= best_time):
            best_time = time_to_buy + time_to_fin
        else:
            break
        N += 1.0
    sys.stdout.write('Case #%d: %.8f\n' % (i, best_time))