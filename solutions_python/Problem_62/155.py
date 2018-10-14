f = open('A-large.in', 'r')
T = int(f.readline().strip())
for case in range(T):
    N = int(f.readline().strip())
    ws = []
    for i in range(N):
        ws.append(map(int, f.readline().strip().split()))
    ws.sort()
    int_count = 0
    #counts = [0] * N
    for i in range(N):
        a, b = ws[i]
        for j in range(i + 1, N):
            c, d = ws[j]
            if d < b:
                int_count += 1
    print "Case #%d: %d" % (case + 1, int_count)
            
        
