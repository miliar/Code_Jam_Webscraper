T = int(raw_input())

for case in range(1, T+1):
    D , N = raw_input().split()
    D = int(D)
    N = int(N)

    time_taken_i = []
    speed_i = []
    print "Case #%d:" % case,   
    for horse in range(N):
        ki, si = raw_input().split()
        ki = int(ki)
        si = int(si)

        time_taken_i.append((D-ki)/(si*1.0))
        speed_i.append(round((D-ki)/(si*1.0), 6))
        

    index_max = time_taken_i.index(max(time_taken_i))
    
    speed = speed_i[index_max]

    print "%.6f" % (D/speed)
