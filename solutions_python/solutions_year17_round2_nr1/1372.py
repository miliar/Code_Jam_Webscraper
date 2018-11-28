import sys

f = open(sys.argv[1])
T = int(f.readline())
for i in range(T):
    t = 0.0
    d, n = f.readline().split(' ')
    d, n = float(d), int(n)
    for j in range(n):
        k, s = f.readline().split(' ')
        k, s = float(k), float(s)
        t = max(t, (d-k)/s)
    print 'Case #%d: %.6f' %(i+1, d / t)
        
    
