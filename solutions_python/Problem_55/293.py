f = open('C-small-attempt0.in', 'r')
fout = open('C-small-attempt0.out', 'w')
T = int(f.readline().strip())
for c in range(T):
    line = f.readline().strip().split()
    R = int(line[0])
    k = int(line[1])
    N = int(line[2])
    line = f.readline().strip().split()
    gs = [int(line[i]) for i in range(N)]
    
    gi = 0
    total_euros = 0
    for run in range(R):
        open_seats = k
        starting_gi = gi
        while gs[gi] <= open_seats:
            open_seats -= gs[gi]
            gi = (gi + 1) % N
            if gi == starting_gi:
                #print "empty queue"
                break
        total_euros += (k - open_seats)
    
    fout.write('Case #%d: ' % (c+1))
    fout.write(str(total_euros))
    fout.write('\n')
    
    
    
