

fname = 'B-small-attempt1.in'

f = open(fname, 'r')
T = int(f.readline())
for t in range(T):
    time = []
    dist = []
    acc = []
    ln = f.readline().split()
    D = float(ln[0])
    N = int(ln[1])
    A = int(ln[2])
    for n in range(N):
        ln = f.readline().split()
        time.append(float(ln[0]))
        dist.append(float(ln[1]))
    
    ln = f.readline().split()
    acc = [ float(a) for a in ln ]
    for n in range(1, N+1):
        if (dist[n-1] > D):
            if (n > 1):
                v = (dist[n-1] - dist[n-2])/(time[n-1] - time[n-2])
                dist[n-1] = D
                time[n-1] = time[n-2] + (D - dist[n-2]) / v
            else:
                dist[n-1] = D
            N = n
            break

    
    print 'Case #%d:' % (t+1)
    for a in acc:
        st = 0.0
        ti = 0.0
        for n in range(N-1):
            if (st + 0.5 * a * (time[n+1] - ti) ** 2) > dist[n+1]:
                ti = time[n+1]
                st = dist[n+1]
            else:
                ti = ti + (2*(dist[n+1]-st)/a) ** 0.5
                st = dist[n+1]
        if N == 1:
                ti = ti + (2*(dist[0]-st)/a) ** 0.5
                st = dist[0]
            
        print ti
f.close()
