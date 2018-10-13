P = [1, 4, 9, 121, 484] #calculated manually
f = open('C-small-attempt0.in')
T = int(f.readline().strip())
for t in range(T):
    (N,M) = f.readline().split(' ');
    (N,M) = (int(N), int(M))
    c = 0
    for p in P:
        if N <= p and p <= M:
            c = c + 1
    print "Case #" + str(t + 1) + ": "  + str(c)
