import sys
fid = open(sys.argv[1])
T = int(fid.next().strip())
for i in range(T):
    R, k, N = map(int, fid.next().strip().split())
    g = map(int, fid.next().strip().split())
    tsum = 0
    j = 0
    q = N
    for r in range(R):
        csum = 0
        q = N
        while g[j] + csum <= k and q > 0:
            csum += g[j]
            j = (j+1)%N
            q = q - 1
        tsum += csum
    print 'Case #'+str(i+1)+': '+str(tsum)
        
